# İlerleme Durumu - Görev Panosu



## Yapılacaklar (TO-DO)

- `[X]` `requirements.txt` dosyasına `selenium` ve `webdriver-manager` ekle.
- `[X]` `scrapers/` klasör yapısını oluştur.
- `[X]` `base_scraper.py` soyut sınıfını yaz (abstract base class).
- `[X]` Mevcut kodu `requests_scraper.py` modülüne taşı ve refactor et.
- `[X]` `selenium_scraper.py` modülünü oluştur (WebDriver yönetimi, bekleme stratejileri).
- `[X]` `config/sites_config.json` dosyasını oluştur (Hepsiburada, Trendyol, N11 için seçiciler).
- `[~]` Ana `scraper.py` dosyasını hibrit mimariye göre güncelle (mod seçimi, factory pattern).
- `[ ]` Selenium ile Hepsiburada'dan veri çekmeyi test et.
- `[ ]` Trendyol ve N11 için test et ve CSS seçicilerini ayarla.
- `[ ]` Headless mod desteği ekle ve test et.
- `[ ]` Kullanıcı dokümantasyonunu güncelle (README.md).
- `[ ]` Tüm değişiklikleri commit edip GitHub'a push et.

### Gelecek Geliştirmeler
- `[ ]` CSV/JSON çıktı formatları ekle.
- `[ ]` Daha fazla veri alanı ekle (ürün puanı, yorum sayısı, resim URL'si).
- `[ ]` Rate limiting (istekler arası gecikme) ekle.
- `[ ]` Unit testler yaz.


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
