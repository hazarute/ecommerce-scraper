# progress.md — İlerleme Durumu (Bellek Bankası)

## Güncelleme: Bellek Bankası Yeniden Tasarımı (14 Nov 2025)

### Tamamlandı (DONE)
- [X] `/.memory-bank/` içindeki tüm ana dokümanların yeniden yazılması ve yeni protokole uygun hale getirilmesi (`projectbrief.md`, `productContext.md`, `activeContext.md`, `systemPatterns.md`, `techContext.md`, `progress.md`).
- [X] `custom_plugins/_template.py` ve `custom_plugins/README.md` dosyalarının oluşturulması (repo içinde mevcut).
- [X] `core/` ve `utils/` dizinlerinin oluşturulması (kök yapıyı kullanıcı oluşturdu).

### Devam Ediyor (IN PROGRESS)
- [ ] `scrapers/` içeriğinin `core/scrapers/` altına `git mv` ile taşınması — fiziksel taşıma/commit bekliyor (taşıma planı hazır; onay bekleniyor).

### Gelecek (TODO)
- [ ] `app.py` Streamlit wireframe ve `core.engine` entegrasyonu.
- [ ] `utils/exporters.py` ile CSV/JSON exporter'ların uygulanması ve test edilmesi.
- [ ] `requirements.txt` güncellemesi (`streamlit` eklenmesi) ve dependency testleri.
- [ ] Unit testler, linter ve CI pipeline entegrasyonu.

### Bilinen Riskler
- [!] `custom_plugins` dinamik importu güvenlik riski taşır — production ortamında sandbox veya izole çalışma önerilir.
- [!] Anti-bot engelleri (Cloudflare, CAPTCHA) bazı sitelerde scraping başarısını etkileyebilir; çözüm için proxy, davranış simülasyonu veya insan müdahalesi gerekebilir.

### Notlar
- Bu `progress.md` dosyası belleğin “fiziksel durumunu” gösterir ve 14 Nov 2025 tarihinde güncellenmiştir.

### Change Log
- 14 Nov 2025 — Bellek güncellemesi: kullanıcı yeni dosya yapısını oluşturdu; taşıma adımı (`git mv`) onaya açık. (Yapıldı: memory update by assistant per user's instruction)