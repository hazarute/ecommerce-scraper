# progress.md — İlerleme Durumu (Bellek Bankası)

## Güncelleme: V2.0 Yayın ve Dönüşüm (14 Nov 2025)

### Tamamlandı (DONE)
- [X] `/.memory-bank/` içindeki ana dokümanların yeni protokole göre güncellenmesi.
- [X] Legacy `scrapers/` içeriğinin modernize edilerek `core/scrapers/` altına eklenmesi (`base`, `requests`, `selenium`).
- [X] `custom_plugins/_template.py` ve `custom_plugins/README.md` eklenmesi.
- [X] `requirements.txt`'e `streamlit` eklenmesi.
- [X] Tüm değişikliklerin commit edilip `main` dalına pushlanması.
- [X] Annotated tag `v2.0.0` oluşturulup `origin`'e pushlandı.
 - [X] `utils/fileops.py` eklendi ve `save_to_csv` / `save_html_debug` fonksiyonları uygulandı.
 - [X] `pandas` `requirements.txt`'e eklendi.
 - [X] `core/engine.py` eklendi (plugin discovery + run_job).
 - [X] `app.py` Streamlit wireframe eklendi ve commit/push yapıldı.
 - [X] `utils/exporters.py` eklendi (CSV/JSON exporter).
 - [X] `app.py` site-config entegrasyonu ile güncellendi (config/sites_config.json).
 - [X] CI workflow eklendi: `.github/workflows/ci.yml` (smoke import test).
 - [X] `app.py` modern UI tasarımı tamamlandı: sekmeli yapı, sidebar iyileştirmesi, session state, metrikler, interaktif tablo, status spinner.
 - [X] Smoke test başarıyla geçti (6/6): kütüphaneler, core modülleri, konfigürasyon, dizinler, syntax, plugin discovery.
 - [X] Kategori sayfaları ile konfigürasyon güncellendi (hepsiburada/laptop, n11/laptop, trendyol/laptop).
 - [X] Selector algılama hatası düzeltildi: URL'den site AUTO-DETECT, manual input'ta selector'lar yüklenmesi sağlandı (Commit: 62a19ca).
 - [X] Plugin Selector Architecture (OPTION 2 - Ayrı .json) uygulandı (Commit: 20b8a82):
   - `_template.py`: `_load_selectors_from_json()` fonksiyonu
   - `example_amazon.py` + `example_amazon.json`: Production-ready örnek
   - `core/engine.py`: `_load_plugin_config()` eklendi
   - `custom_plugins/README.md`: Müşteri kılavuzu
 - [X] N11 anti-bot debugging ve fix (Commit: 75a6128):
   - `tests/debug_n11.py`: N11 selektör ve erişim test scripti
   - Root cause tespit: N11 requests library'yi blokluyor (403 Forbidden)
   - Çözüm: app.py'de URL'den site algılanıp mode otomatik Selenium'a ayarlanıyor
   - Sidebar'da algılanan site + mod bilgisi gösteriliyor
 - [X] Integration tests ve Cloudflare blocking tespiti (Commit: e80aedb):
   - `tests/test_n11_integration.py`: N11 URL detection ✅ + scraping ❌
   - `tests/test_hepsiburada_jsonld.py`: Hepsiburada JSON-LD ✅ + scraping ❌
   - `tests/TEST_REPORT_N11.md`: Comprehensive test report
   - Finding: Tüm sitelerde anti-bot koruma (Cloudflare, redirects) aktif

### Devam Ediyor (IN PROGRESS)

### Gelecek (TODO)
- [ ] **DECISION:** Anti-bot bypass stratejisini seç (proxy/undetected-chromedriver/API)
- [ ] **IMPL:** Seçilen stratejiyi implement et
- [ ] **TEST:** N11/Hepsiburada ile tekrar test
- [ ] Unit testler ve linter kurulumu (pytest, flake8).
- [ ] Plugin güvenliği için sandbox/manifest politika taslaması ve testleri.

### Bilinen Riskler
- [!] `custom_plugins` dinamik importu güvenlik riski taşır — production ortamında sandbox veya izole çalışma önerilir.
- [!] Anti-bot engelleri (Cloudflare, CAPTCHA) bazı sitelerde scraping başarısını etkileyebilir; çözüm için proxy, davranış simülasyonu veya insan müdahalesi gerekebilir.

### Notlar
- Bu `progress.md` dosyası belleğin “fiziksel durumunu” gösterir ve 14 Nov 2025 tarihinde güncellenmiştir.

### Change Log
- 14 Nov 2025 (Saat: ~14:30) — v2.0.0 yayımlandı: Streamlit + plugin mimarisi göçü tamamlandı.
- 14 Nov 2025 (Saat: ~15:00) — **YENİDEN PLANLA:** UX tasarımı iterasyonu başlatıldı.
- 14 Nov 2025 (Saat: ~16:30) — Modern UI tasarımı tamamlandı + Smoke test: 6/6 ✅
- 14 Nov 2025 (Saat: ~17:00) — Kategori sayfaları güncellendi + AUTO-DETECT bug fix
- 14 Nov 2025 (Saat: ~18:00) — Plugin Selector Architecture (OPTION 2) tamamlandı.
- 14 Nov 2025 (Saat: ~18:45) — N11 anti-bot debugging + mode auto-detection (Commit: 75a6128)
- 14 Nov 2025 (Saat: ~19:30) — Integration tests + Cloudflare blocking discovery (Commit: e80aedb)