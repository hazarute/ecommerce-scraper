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

### Devam Ediyor (IN PROGRESS)
- [ ] `app.py` modern UI tasarımı — sekmeli yapı, sidebar iyileştirmesi, session state, metrikler, interaktif tablo, status spinner.

### Gelecek (TODO)
- [ ] Unit testler ve linter kurulumu (pytest, flake8).
- [ ] Plugin güvenliği için sandbox/manifest politika taslağı ve testleri.
- [ ] Anti-bot stratejileri: proxy, rate-limiting, retry, headless/fingerprint önlemleri ve dokümantasyon.

### Bilinen Riskler
- [!] `custom_plugins` dinamik importu güvenlik riski taşır — production ortamında sandbox veya izole çalışma önerilir.
- [!] Anti-bot engelleri (Cloudflare, CAPTCHA) bazı sitelerde scraping başarısını etkileyebilir; çözüm için proxy, davranış simülasyonu veya insan müdahalesi gerekebilir.

### Notlar
- Bu `progress.md` dosyası belleğin “fiziksel durumunu” gösterir ve 14 Nov 2025 tarihinde güncellenmiştir.

### Change Log
- 14 Nov 2025 (Saat: ~14:30) — v2.0.0 yayımlandı: Streamlit + plugin mimarisi göçü tamamlandı.
- 14 Nov 2025 (Saat: ~15:00) — **YENİDEN PLANLA:** UX tasarımı iterasyonu başlatıldı. `app.py` modern bileşenler (tabs, sidebar, status, metrics, dataframe) ile yeniden tasarlanacak.