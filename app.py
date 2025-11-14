import streamlit as st
import pandas as pd
import time
from pathlib import Path
import json as _json
from core import engine
from utils import exporters

# ================================
# PAGE CONFIG & INITIALIZATION
# ================================
st.set_page_config(
    page_title="E-commerce Product Scraper",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load site configurations
CONFIG_PATH = Path("config") / "sites_config.json"
SITE_CONFIGS = {}
if CONFIG_PATH.exists():
    try:
        SITE_CONFIGS = _json.loads(CONFIG_PATH.read_text(encoding='utf-8'))
    except Exception:
        SITE_CONFIGS = {}

# Initialize session state for data persistence
if "scrape_results" not in st.session_state:
    st.session_state.scrape_results = None
if "last_job_info" not in st.session_state:
    st.session_state.last_job_info = {}

# ================================
# HEADER & TITLE
# ================================
st.markdown("""
<div style='text-align: center;'>
    <h1>🕷️ E-Commerce Product Scraper</h1>
    <p style='color: #888; font-size: 16px;'>Modern ve güvenilir web kazıma çözümü • v2.0</p>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# ================================
# SIDEBAR CONFIGURATION
# ================================
with st.sidebar:
    st.header("⚙️ İş Ayarları")
    
    # Site ve Mode seçimi (temel ayarlar)
    col_site, col_mode = st.columns(2)
    with col_site:
        site_keys = list(SITE_CONFIGS.keys())
        site_choice = st.selectbox(
            "🎯 Hedef Site",
            ["manuel"] + site_keys,
            help="Kaydedilmiş site presetlerini veya manuel URL girişini seçin."
        )
    
    with col_mode:
        mode = st.selectbox(
            "🔧 Kazıma Modu",
            ["requests", "selenium", "plugin"],
            help="requests: Hızlı (statik siteler), selenium: Dinamik siteler, plugin: Özel modüller"
        )
    
    # URL giriş — site seçilmişse varsayılan değer config'den gelir
    if site_choice != "manuel":
        site_conf = SITE_CONFIGS.get(site_choice, {})
        default_url = site_conf.get('url', "https://example.com/")
        url = st.text_input(
            "🔗 Target URL",
            value=default_url,
            help=f"Site: {site_choice} — Config'ten otomatik yüklendi"
        )
    else:
        url = st.text_input(
            "🔗 Target URL",
            value="https://example.com/",
            placeholder="https://example.com/products",
            help="Manuel URL girişi — selector'ları manuel seçmeniz gerekecek"
        )
    
    # Gelişmiş Ayarlar (gizli expander)
    with st.expander("⚙️ Gelişmiş Ayarlar"):
        if mode == "selenium":
            headless = st.checkbox("Headless Mode", value=True, help="Tarayıcı penceresini açmaz.")
            timeout = st.number_input("İstek Zaman Aşımı (sn)", min_value=5, max_value=60, value=30)
        else:
            headless = True
            timeout = 30
        
        user_agent_preset = st.selectbox(
            "User-Agent Seçimi",
            ["Varsayılan", "Chrome (Desktop)", "Safari (iOS)"],
            help="Sunucu tarafında engelleme riskini azaltır."
        )
    
    # Plugin seçimi (mode='plugin' ise görün)
    plugins = engine.discover_plugins()
    plugin_choice = None
    if mode == "plugin":
        if plugins:
            plugin_options = [p.get("module") for p in plugins]
            plugin_choice = st.selectbox("📦 Plugin Seçimi", plugin_options)
        else:
            st.warning("📦 Hiçbir plugin yüklenmedi.")
    
    # Seçim yapılmış sitenin selector'larını yükle
    # Eğer site="manuel" ise, URL'den site adını çıkarmaya çalış
    selectors = {}
    detected_site = site_choice
    detected_mode = mode  # Mode da detect edilecek
    
    if site_choice == "manuel" and url:
        # URL'den site adını otomatik algıla
        if "hepsiburada" in url.lower():
            detected_site = "hepsiburada"
            detected_mode = "selenium"  # Hepsiburada Selenium gerektiriyor
        elif "trendyol" in url.lower():
            detected_site = "trendyol"
            detected_mode = "selenium"  # Trendyol Selenium gerektiriyor
        elif "n11" in url.lower():
            detected_site = "n11"
            detected_mode = "selenium"  # N11 bot engelleme var, Selenium şart
    
    # Algılanan veya seçilen siteden selector'ları yükle
    if detected_site != "manuel":
        site_conf = SITE_CONFIGS.get(detected_site, {})
        selectors = site_conf.get('selectors', {})
        selectors['site'] = detected_site
        
        # Eğer manuel URL ise ve siteden farklı bir site algılandıysa, bilgi ver
        if site_choice == "manuel":
            mode_text = f" (Mod: **{detected_mode.upper()}**)" if detected_mode != mode else ""
            st.sidebar.info(f"ℹ️ URL'den algılanan site: **{detected_site.upper()}**{mode_text}\n— Seçiciler ve mode otomatik yüklendi")
    elif site_choice == "manuel":
        st.sidebar.warning("⚠️ Site algılanamadı. Selector'ları manuel girmeniz gerekecek.")
    
    # Override mode if detected
    mode = detected_mode
    
    st.markdown("---")
    
    # RUN Butonu (prominent)
    run_btn = st.button(
        "🚀 Kazımayı Başlat",
        key="run_scrape",
        type="primary",
        use_container_width=True
    )
    
    st.markdown("---")
    
    # About
    st.markdown("""
    **ℹ️ Hakkında**
    - Versiyon: **v2.0.0**
    - Yapımcı: Yazılım Ekibi
    - Lisans: MIT
    """)

# ================================
# MAIN TABS
# ================================
tab1, tab2, tab3 = st.tabs(["🚀 Kazıma Paneli", "🧩 Eklenti Merkezi", "📂 Veri Geçmişi"])

# ================================
# TAB 1: SCRAPING PANEL
# ================================
with tab1:
    if run_btn:
        # Clear previous results
        st.session_state.scrape_results = None
        st.session_state.last_job_info = {}
        
        # Status container with progress
        with st.status("🔄 İşlem Yapılıyor...", expanded=True) as status:
            try:
                # Step 1: Site bağlantısı
                st.write("📍 Hedef siteye bağlanılıyor...")
                time.sleep(0.5)
                
                # Step 2: Veri çekiliyor
                st.write("📊 Ürün verileri çekiliyor...")
                time.sleep(0.5)
                
                # ACTUAL JOB EXECUTION
                results, err = engine.run_job(
                    url,
                    mode,
                    selectors=selectors,
                    plugin_module=plugin_choice,
                    headless=headless
                )
                
                if err:
                    st.error(f"❌ Hata: {err}")
                    status.update(label="❌ İşlem Başarısız", state="error")
                else:
                    # Step 3: Veriler işleniyor
                    st.write("⚙️ Veriler işleniyor...")
                    time.sleep(0.3)
                    
                    # Store results in session
                    st.session_state.scrape_results = results
                    st.session_state.last_job_info = {
                        "site": site_choice,
                        "mode": mode,
                        "url": url,
                        "count": len(results)
                    }
                    
                    # Step 4: Export
                    st.write("💾 Dosyalar kaydediliyor...")
                    exporters.export_csv(results)
                    exporters.export_json(results)
                    time.sleep(0.3)
                    
                    st.write("✅ Kazıma tamamlandı!")
                    status.update(label="✅ İşlem Başarılı", state="complete")
            
            except Exception as e:
                st.error(f"❌ İşlem sırasında hata: {str(e)}")
                status.update(label="❌ İşlem Başarısız", state="error")
    
    # DISPLAY RESULTS (from session state)
    if st.session_state.scrape_results is not None:
        st.balloons()
        st.toast("✨ Kazıma başarılı!", icon="✅")
        
        st.markdown("---")
        
        # Metrics row
        results = st.session_state.scrape_results
        job_info = st.session_state.last_job_info
        
        col_metrics = st.columns(4)
        with col_metrics[0]:
            st.metric("📦 Toplam Ürün", job_info.get("count", 0))
        
        if results:
            df = pd.DataFrame(results)
            
            # Calculate metrics if price column exists
            if 'price' in df.columns:
                try:
                    # Convert to numeric if possible
                    df['price_numeric'] = pd.to_numeric(df['price'], errors='coerce')
                    avg_price = df['price_numeric'].mean()
                    min_price = df['price_numeric'].min()
                    max_price = df['price_numeric'].max()
                    
                    with col_metrics[1]:
                        st.metric("💰 Ort. Fiyat", f"${avg_price:.2f}" if not pd.isna(avg_price) else "N/A")
                    with col_metrics[2]:
                        st.metric("📉 En Düşük", f"${min_price:.2f}" if not pd.isna(min_price) else "N/A")
                    with col_metrics[3]:
                        st.metric("📈 En Yüksek", f"${max_price:.2f}" if not pd.isna(max_price) else "N/A")
                except Exception:
                    pass
        
        st.markdown("---")
        
        # Data table with column configuration
        st.subheader("📋 Sonuç Tablosu")
        if results:
            try:
                df_display = pd.DataFrame(results)
                
                # Configure columns if images exist
                col_config = {}
                if 'image_url' in df_display.columns:
                    col_config['image_url'] = st.column_config.ImageColumn("Resim", width="small")
                
                st.dataframe(
                    df_display,
                    use_container_width=True,
                    column_config=col_config,
                    hide_index=False
                )
            except Exception as e:
                # Fallback: show as raw JSON
                st.json(results)
        
        st.markdown("---")
        
        # Download buttons
        st.subheader("💾 İndirme Seçenekleri")
        col_dl1, col_dl2 = st.columns(2)
        
        with col_dl1:
            csv_bytes = pd.DataFrame(results).to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 CSV İndir",
                data=csv_bytes,
                file_name=f"scrape_results_{job_info.get('site', 'manual')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        
        with col_dl2:
            json_str = _json.dumps(results, indent=2, ensure_ascii=False).encode('utf-8')
            st.download_button(
                label="📥 JSON İndir",
                data=json_str,
                file_name=f"scrape_results_{job_info.get('site', 'manual')}.json",
                mime="application/json",
                use_container_width=True
            )

# ================================
# TAB 2: PLUGIN CENTER
# ================================
with tab2:
    st.header("🧩 Eklenti Merkezi")
    
    if plugins:
        for idx, plugin in enumerate(plugins):
            with st.container(border=True):
                module_name = plugin.get("module", "Unknown")
                metadata = plugin.get("metadata") or {}
                
                col_name, col_version = st.columns([3, 1])
                with col_name:
                    st.subheader(f"📦 {metadata.get('name', module_name)}")
                with col_version:
                    st.caption(f"v{metadata.get('version', '?')}")
                
                st.write(metadata.get('description', 'Açıklama yok'))
                
                # Details
                col_sites, col_status = st.columns(2)
                with col_sites:
                    supported = metadata.get('supported_sites', [])
                    if supported:
                        st.write(f"🎯 **Desteklenen Siteler:** {', '.join(supported)}")
                
                with col_status:
                    st.success("✅ Aktif ve Hazır")
    else:
        st.info("📦 Şu anda hiçbir eklenti yüklenmedi. `custom_plugins/` klasörüne `.py` dosyaları ekleyin.")

# ================================
# TAB 3: DATA HISTORY
# ================================
with tab3:
    st.header("📂 Veri Geçmişi")
    
    # Check for saved exports
    exports_path = Path("data/exports")
    if exports_path.exists():
        files = sorted(exports_path.glob("*"), key=lambda x: x.stat().st_mtime, reverse=True)
        if files:
            st.success(f"✅ {len(files)} dosya bulundu.")
            for file in files[:10]:  # Show last 10
                col_name, col_size, col_action = st.columns([2, 1, 1])
                with col_name:
                    st.write(f"📄 `{file.name}`")
                with col_size:
                    size_kb = file.stat().st_size / 1024
                    st.caption(f"{size_kb:.1f} KB")
                with col_action:
                    with open(file, "rb") as f:
                        st.download_button(
                            "⬇️",
                            f,
                            file_name=file.name,
                            key=f"dl_{file.name}"
                        )
        else:
            st.info("📂 Henüz hiçbir dışa aktarım dosyası yok.")
    else:
        st.info("📂 Dışa aktarım klasörü bulunamadı. İlk kazımayı çalıştırın.")
