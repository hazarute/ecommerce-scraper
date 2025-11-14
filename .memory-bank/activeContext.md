# activeContext.md — Aktif Bağlam (Bellek Bankası)

## Amaç
Bu dosya projenin o anki "zihinsel durumu"dur: hangi modüller, hangi sorunlar, hangi kararlar ve nedenleri. Bu bir yapılacaklar listesi değil; kısa ve net bir özet olmalıdır.

## Güncel Durum (14 Nov 2025 — UX Tasarımı Aşaması)
- **Proje Evresi:** v2.0.0 altyapısı tamamlandı; şimdi **Streamlit UI'sinin modern ve kullanıcı-odaklı tasarımına geçiliyor**.
- **Fokus:** `app.py` tamamen yeniden tasarlanacak — görsel hiyerarşi, sekmeli yapı, sidebar iyileştirmesi, session state yönetimi ve akıllı geri bildirim (spinner, toast, metrikler).
- **Odak Modülü:** `app.py` — Streamlit bileşenleri (st.tabs, st.sidebar, st.status, st.metric, st.dataframe, st.metric, column_config) entegrasyonu.
- **Mevcut Durum:** 
  - `core/`, `custom_plugins/`, `utils/` modülleri stabil ve hazır.
  - `config/sites_config.json` ile site presetleri ve seçiciler mevcut.
  - `utils/exporters.py` ve `utils/fileops.py` fonksiyonel.
  - Mevcut minimal `app.py` daha gelişmiş tasarımla değiştirilecek.
- **Teknik Stack Güncellemesi:** `pandas` (metrikler, veri işleme), `time` (gecikmeler ve loglamalar), mevcut `core.engine` ve `utils` importları korunacak.

 - Yeni Kod Eklentileri (14 Nov 2025):
	 - `utils/fileops.py` eklendi: `save_to_csv` ve `save_html_debug` fonksiyonları eklendi (pandas bağımlılığı eklendi).
	 - `core/engine.py` eklendi: plugin discovery (`discover_plugins`) ve job orchestration (`run_job`) fonksiyonları.
	 - `app.py` eklendi: minimal Streamlit wireframe — mode seçimi, URL girişi, plugin seçimi ve Run butonu ile sonuç gösterimi + CSV export.
	 - `requirements.txt` güncellendi: `streamlit` ve `pandas` eklendi.
   - `utils/exporters.py` eklendi: `export_csv` ve `export_json` fonksiyonları uygulandı.
   - `app.py` güncellendi: `config/sites_config.json` entegrasyonu eklendi (site presetleri ile selectors doldurma).
   - CI: `.github/workflows/ci.yml` eklendi — requirements kurulumu ve temel import smoke testi çalıştırılıyor.

## Kararlar (Onay Bekleyen / Onaylanan)
 - Onaylanan: Bellek bankası güncellendi ve taşınma ile ilgili değişiklikler repoya işlendi.
 - Onaylanan: Plugin API basit tutulacak: `metadata` + `run(url, config)` → `List[Dict]`.
 - Bekliyor: `custom_plugins` için production sandbox politikası ve manifest zorunlulukları; dağıtıma alınmadan önce güvenlik incelemesi önerilir.

## Son Eylemler (Kısa)
1. `/.memory-bank/` dosyaları yeni protokole göre yeniden yazıldı (tamamlandı).
2. `custom_plugins/_template.py` ve `custom_plugins/README.md` oluşturuldu ve repoya eklendi.

## Tasarım Kararları (14 Nov 2025 — UX İterasyonu)
- **Sekmeli Yapı:** 3 tab (Kazıma, Eklenti, Veri Geçmişi) → kullanıcı cognitive load'ını azaltacak.
- **Sidebar Organizasyonu:** Site + Mode temelinde, gelişmiş ayarlar expander'da gizli → temiz ve professional.
- **Session State:** Kazıma sonuçları session'da kalacak → sekme geçişleri sırasında veri kaybolmayacak.
- **Feedback Loop:** `st.status` spinner + adım loglar + `st.toast/balloons` başarı → modern UX best practice.
- **Metrikler ve Veri Görselleştirme:** Pandas ile özet kartlar (`st.metric`) + interaktif tablo (`st.dataframe` + `ImageColumn`) → professional ve actionable.

## Notlar ve Kanıtlar
- Bu güncelleme: 14 Nov 2025 — Mimar "UX Tasarımı" komutu verdi. `app.py` modern bileşenlerle yeniden tasarlanacak.
- Mevcut `core/` ve `utils/` modülleri değişmeyecek; sadece `app.py` UI layer yenilenmesi.
- Tüm teknik detaylar `systemPatterns.md` ve `techContext.md`'de tutarlı tutulacak.