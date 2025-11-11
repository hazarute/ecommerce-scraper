
# Aktif Bağlam - Strateji Defteri

## Mevcut Çalışma Odağı
Tüm mimari güncellemeler başarıyla tamamlandı ve GitHub'a push edildi. Şu anki odak: Gerçek veri çekilememesi sorununu çözmek için anti-bot ve selector engellerini aşmaya yönelik debug ve iyileştirme stratejileri geliştirmek.
## Öğrenilenler ve İçgörüler

- Requests ve Selenium ile yapılan tüm denemelerde demo veri dışında gerçek ürün verisi çekilemiyor.
- Büyük e-ticaret siteleri (Hepsiburada, Trendyol, N11) güçlü anti-bot korumaları (Cloudflare, Captcha, JS challenge, cookie, headless tespiti) kullanıyor.
- Seçiciler (CSS selector) muhtemelen güncel site yapısıyla uyuşmuyor veya dinamik yüklenen içerikler alınamıyor.


## Aktif Kararlar ve Gerekçeler

1.  **Kodun Modülerleştirilmesi:**
    *   **Karar:** Kod, scrapers/ klasörüne bölünüyor; base_scraper.py ile soyut taban sınıf, requests_scraper.py ve selenium_scraper.py ile iki ayrı modül oluşturuluyor.
    *   **Gerekçe:** Sürdürülebilirlik, test edilebilirlik ve yeni scraping stratejilerinin kolay eklenmesi.

2.  **Hibrit Mimari ve Mod Seçimi:**
    *   **Karar:** Kullanıcıdan çalışma anında Requests (hızlı, basit) veya Selenium (gelişmiş, anti-bot) seçimi alınacak. Gelecekte otomatik mod (akıllı/hybrid) eklenebilir.
    *   **Gerekçe:** Farklı siteler ve engel seviyeleri için esneklik, eğitimsel değer.

3.  **Siteye Özel Yapılandırma:**
    *   **Karar:** CSS seçiciler ve site ayarları config/sites_config.json dosyasına taşınıyor.
    *   **Gerekçe:** Kodun sadeleşmesi, yeni site eklemenin kolaylaşması.

4.  **Selenium ve WebDriver Yönetimi:**
    *   **Karar:** WebDriver yönetimi için webdriver-manager kullanılıyor, headless mod ve User-Agent desteği ekleniyor.
    *   **Gerekçe:** Anti-bot sistemlerini aşmak ve sunucu ortamlarında çalışabilirlik.

5.  **Gelişmiş Hata Yönetimi:**
    *   **Karar:** HTTP hata kodlarına göre detaylı mesajlar, demo veri fallback.
    *   **Gerekçe:** Kullanıcı deneyimi ve eğitimsel açıklık.



- Projenin ilk safhasında kullanılan temel scraper.py kodu, referans ve tarihsel izlenebilirlik için memory-bank/scraper_v1_archive.md dosyasına arşivlendi. Kodun evrimi ve mimari dönüşüm süreci belgelendi.


### Son İlerlemeler


- Hepsiburada için güncel HTML analiz edildi, yeni ürün kartı seçicileri belirlendi ve config dosyasına eklendi.
- selenium_scraper.py'da product_container None olduğunda tüm sayfada ürün arayacak şekilde kod güncellendi.
- fetch() ile kaydedilen ve parse edilen HTML birebir aynı olduğu doğrulandı.
- parse fonksiyonuna debug print eklendi ve selectorların None geldiği tespit edildi.
- scraper.py'da manuel URL girildiğinde kullanıcıdan selector seçimi alınacak şekilde güncellendi.
- Sonuç: Gerçek ürün verisi başarıyla çekiliyor, scraping akışı ve selector yönetimi tamamen stabil.



### Yeni Stratejik Plan (Kasım 2025)
1. Selenium ile çekilen sayfa kaynağını dosyaya kaydedip, gerçekten ürün listesi geliyor mu kontrol et (anti-bot/captcha/JS engeli var mı?).
2. Güncel HTML'e göre doğru CSS seçicileri bul ve config dosyasını güncelle.
3. Gerekirse Selenium'da insan davranışı simülasyonu (scroll, mouse hareketi, tıklama), header/cookie ayarları ve bekleme süresi artırımı uygula.
4. Hala veri çekilemiyorsa, alternatif anti-bot aşma tekniklerini araştır (proxy, oturum açma, farklı browser profili, vs).
5. Tüm bulguları ve ilerlemeleri bellek bankasında ve dokümantasyonda güncel tut.
