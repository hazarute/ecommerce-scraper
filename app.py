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
# SIDEBAR CONFIGURATION (PLUGIN-FIRST)
# ================================
with st.sidebar:
    st.header("⚙️ İş Ayarları")

    # 1. Kazıma Yöntemi Seçimi
    scrape_method = st.radio(
        "Kazıma Yöntemi",
        ["🧩 Siteye Özel Plugin", "🌐 Manuel / Genel"],
        index=0,
        help="Plugin ile (önerilen) veya manuel Requests/Selenium ile kazıma"
    )

    mode = None
    plugin_choice = None
    url = ""
    selectors = None
    plugin_metadata = None

    if scrape_method == "🧩 Siteye Özel Plugin":
        # Plugin seçimi
        plugins = engine.discover_plugins()
        if plugins:
            plugin_options = [p.get("module") for p in plugins]
            plugin_choice = st.selectbox("📦 Plugin Seçimi", plugin_options)
            # Metadata göster
            selected_plugin = next((p for p in plugins if p.get("module") == plugin_choice), None)
            plugin_metadata = selected_plugin.get("metadata") if selected_plugin else {}
            if plugin_metadata:
                st.caption(f"**Versiyon:** {plugin_metadata.get('version', '?')}")
                supported = plugin_metadata.get('supported_sites', [])
                if supported:
                    st.info(f"🎯 Desteklenen Siteler: {', '.join(supported)}")
                desc = plugin_metadata.get('description')
                if desc:
                    st.caption(desc)
            # URL input (örnek varsa placeholder)
            example_url = ""
            if plugin_metadata:
                example_url = plugin_metadata.get("example_url", "")
            url = st.text_input(
                "🔗 Hedef URL",
                value=example_url or "",
                placeholder=example_url or "https://example.com/products",
                help="Kazıma yapılacak ürün listeleme sayfası"
            )
            mode = "plugin"
        else:
            st.warning("📦 Hiçbir plugin yüklenmedi. `custom_plugins/` klasörüne `.py` dosyaları ekleyin.")
            url = ""
            mode = None

    elif scrape_method == "🌐 Manuel / Genel":
        # Requests/Selenium seçimi
        tech = st.selectbox(
            "Teknoloji",
            ["Requests", "Selenium"],
            help="Requests: hızlı, Selenium: dinamik/anti-bot"
        )
        url = st.text_input(
            "🔗 Hedef URL",
            value="https://example.com/products",
            placeholder="https://example.com/products",
            help="Kazıma yapılacak ürün listeleme sayfası"
        )
        mode = "requests" if tech == "Requests" else "selenium"

        # Hazır selector şablonları
        selector_templates = {
            "Boş (Elle Gir)": {"product_item": "", "product_name": "", "product_price": ""},
            "N11 (örnek)": {
                "product_item": "li.column",
                "product_name": "h3.productName",
                "product_price": "div.proDetail span.newPrice ins"
            },
            "Trendyol (örnek)": {
                "product_item": "div.p-card-wrppr",
                "product_name": "div.p-card-chldrn-cntnr span.prdct-desc-cntnr-name.hasRatings",
                "product_price": "div.prc-box-dscntd"
            }
        }
        selected_template = st.selectbox(
            "Hazır Selector Şablonu",
            list(selector_templates.keys()),
            index=0,
            help="Bir siteye uygun hazır şablon seçebilir veya elle girebilirsiniz."
        )
        default_selectors = selector_templates[selected_template]
        st.caption("Aşağıdaki alanları doldurun veya şablonu seçin.")
        product_item = st.text_input("Ürün Kapsayıcı Selector (product_item)", value=default_selectors["product_item"])
        product_name = st.text_input("Ürün Adı Selector (product_name)", value=default_selectors["product_name"])
        product_price = st.text_input("Ürün Fiyatı Selector (product_price)", value=default_selectors["product_price"])
        selectors = {
            "product_item": product_item,
            "product_name": product_name,
            "product_price": product_price
        }

    # Gelişmiş Ayarlar (her iki modda da)
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

    st.markdown("---")

    # RUN Butonu
    run_btn = st.button(
        "🚀 Kazımayı Başlat",
        key="run_scrape",
        type="primary",
        use_container_width=True,
        disabled=(not url or not mode)
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
    if run_btn and url and mode:
        # Clear previous results
        st.session_state.scrape_results = None
        st.session_state.last_job_info = {}

        # Status container with progress
        with st.status("🔄 İşlem Yapılıyor...", expanded=True) as status:
            try:
                st.write("📍 Hedef siteye bağlanılıyor...")
                time.sleep(0.5)
                st.write("📊 Ürün verileri çekiliyor...")
                time.sleep(0.5)

                # ACTUAL JOB EXECUTION
                if mode == "plugin":
                    results, err = engine.run_job(
                        url,
                        mode,
                        selectors={},
                        plugin_module=plugin_choice,
                        headless=headless
                    )
                else:
                    # Manuel/generic modda selectors her zaman dict olarak gönderilmeli
                    # Gelişmiş ayarlardan user-agent ve timeout alınabilir
                    # Şimdilik user_agent_preset sadece string olarak aktarılıyor
                    results, err = engine.run_job(
                        url,
                        mode,
                        selectors=selectors or {},
                        plugin_module=None,
                        headless=headless
                    )

                if err:
                    st.error(f"❌ Hata: {err}")
                    status.update(label="❌ İşlem Başarısız", state="error")
                else:
                    st.write("⚙️ Veriler işleniyor...")
                    time.sleep(0.3)
                    st.session_state.scrape_results = results
                    st.session_state.last_job_info = {
                        "site": plugin_choice if mode == "plugin" else "manuel",
                        "mode": mode,
                        "url": url,
                        "count": len(results)
                    }
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
            if 'price' in df.columns:
                try:
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
    plugins = engine.discover_plugins()
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
    exports_path = Path("data/exports")
    if exports_path.exists():
        files = sorted(exports_path.glob("*"), key=lambda x: x.stat().st_mtime, reverse=True)
        if files:
            st.success(f"✅ {len(files)} dosya bulundu.")
            for file in files[:10]:
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