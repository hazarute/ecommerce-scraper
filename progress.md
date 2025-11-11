# İlerleme Durumu - Görev Panosu




## Yapılanlar (DONE)

- `[X]` requirements.txt dosyasına selenium ve webdriver-manager eklendi.
- `[X]` scrapers/ klasör yapısı oluşturuldu.
- `[X]` base_scraper.py soyut sınıfı yazıldı.
- `[X]` requests_scraper.py ve selenium_scraper.py modülleri oluşturuldu ve refactor edildi.
- `[X]` config/sites_config.json dosyası ile siteye özel seçiciler ve ayarlar JSON'a taşındı.
- `[X]` Ana scraper.py dosyası hibrit/factory pattern ile güncellendi.
- `[X]` Selenium ile Hepsiburada, Trendyol, N11 scraping testleri yapıldı.
- `[X]` Headless mod desteği eklendi ve test edildi.
- `[X]` Kullanıcı dokümantasyonu (ReadMe.md) güncellendi.
- `[X]` Tüm değişiklikler commit edilip GitHub'a push edildi.


### Gelecek Geliştirmeler
- `[ ]` CSV/JSON çıktı formatları ekle.
- `[ ]` Daha fazla veri alanı ekle (ürün puanı, yorum sayısı, resim URL'si).
- `[ ]` Rate limiting (istekler arası gecikme) ekle.
- `[ ]` Unit testler yaz.

---

**Kasım 2025 Selector Debugging ve Akış Stabilizasyonu Güncellemesi:**
- Hepsiburada'nın güncel HTML yapısı incelendi, yeni ürün kartı seçicileri tespit edildi ve config dosyasına eklendi.
- selenium_scraper.py kodu, product_container None olduğunda tüm sayfada ürün arayacak şekilde güncellendi.
- fetch() ile kaydedilen ve parse edilen HTML birebir aynı olduğu doğrulandı.
- parse fonksiyonuna debug print eklendi ve selectorların None geldiği tespit edildi.
- scraper.py'da manuel URL girildiğinde kullanıcıdan selector seçimi alınacak şekilde güncellendi.
- Sonuç: Gerçek ürün verisi başarıyla çekiliyor, scraping akışı ve selector yönetimi tamamen stabil.


	- `[X]` İlk yazılan scraper.py kodu memory-bank/scraper_v1_archive.md dosyasına arşivlendi.

- `[X]` Proje hedeflerini ve kurallarını anlamak için `ReadMe.md` ve `Rules_MemoryBank.md` dosyaları incelendi.
- `[X]` `projectbrief.md` oluşturuldu.
- `[X]` `productContext.md` oluşturuldu.
- `[X]` `activeContext.md` oluşturuldu.
- `[X]` `systemPatterns.md` oluşturuldu.
- `[X]` `techContext.md` oluşturuldu.
- `[X]` `progress.md` (bu dosya) oluşturuldu ve ilk görevler eklendi.
- `[X]` Proje için temel dizin yapısı oluşturuldu.
- `[X]` `requirements.txt` dosyası oluşturuldu.
- `[X]` Temel `scraper.py` dosyası oluşturuldu.
- `[X]` `scraper.py` içine hedef URL ve HTTP başlıkları (User-Agent) için sabitler eklendi.
- `[X]` Web sitesinden HTML içeriğini çeken fonksiyon yazıldı.
- `[X]` HTML içeriğini ayrıştıran ve ürünleri (isim ve fiyat) çıkaran fonksiyon yazıldı.
- `[X]` Çıkarılan verileri terminalde formatlı bir şekilde yazdıran fonksiyon oluşturuldu.
- `[X]` Veri çekme başarısız olduğunda kullanılacak demo veriler tanımlandı.
- `[X]` Ana program akışı (main block) oluşturularak tüm fonksiyonlar bir araya getirildi.
- `[X]` Hepsiburada, Trendyol, N11 sitelerini varsayılan olarak öneren ve manuel girişe izin veren kullanıcı arayüzü eklendi.
- `[X]` Bellek bankası ve ReadMe güncellemeleri yapıldı.
- `[X]` HTTP hata kodlarına göre detaylı ve açıklayıcı hata mesajları eklendi (403, 404, 429, 5xx, timeout, connection error).
- `[X]` Selenium vs Playwright araştırması yapıldı, Selenium seçildi.
- `[X]` Selenium entegrasyon planı oluşturuldu (`memory-bank/selenium_integration_plan.md`).
- `[X]` Hibrit mimari tasarımı tamamlandı (Requests + Selenium).
- `[X]` Bellek bankası dosyaları Selenium entegrasyonu için güncellendi (`activeContext.md`, `systemPatterns.md`, `techContext.md`, `progress.md`).

## Bilinen Sorunlar (BUGS)

- `[!]` **403 Forbidden Hatası:** Hepsiburada, Trendyol, N11 gibi siteler anti-bot koruması kullanıyor. Basit HTTP istekleri engellenebilir. Selenium/Playwright gibi araçlar gerekebilir.
