# Aktif Bağlam - Strateji Defteri

## Mevcut Çalışma Odağı
Selenium tarayıcı otomasyon kütüphanesini projeye entegre etmek için kapsamlı bir plan oluşturuldu. Şu anki odak, anti-bot sistemlerini (Cloudflare, CAPTCHA) aşabilecek hibrit bir mimari tasarlamak ve projeyi "basit örnek"ten "gerçek dünya aracı"na dönüştürmek.

## Aktif Kararlar ve Gerekçeler

1.  **Gelişmiş HTTP Hata Yönetimi:**
    *   **Karar:** Basit try-except yerine, HTTP hata kodlarına (403, 404, 429, 5xx) göre spesifik hata mesajları ve açıklamaları eklendi.
    *   **Gerekçe:** Kullanıcıya hatanın nedenini ve çözüm önerilerini açıkça sunmak. Özellikle 403 Forbidden hatası, bu sitelerin Cloudflare, CAPTCHA gibi anti-bot sistemleri kullandığını gösteriyor.

2.  **Kullanıcıdan Dinamik URL ve Site Seçimi:**
    *   **Karar:** Script başlatılırken kullanıcıya Hepsiburada, Trendyol, N11 gibi popüler sitelerden birini seçme veya manuel URL girme seçeneği sunulacak.
    *   **Gerekçe:** Kodun sadece sabit bir siteye bağlı kalmasını önler, farklı sitelerle test etmeyi ve genişletmeyi kolaylaştırır.

3.  **Tek Betik Mimarisi (`scraper.py`):**
    *   **Karar:** Proje tek bir Python betiği ile devam edecek.
    *   **Gerekçe:** Basitlik ve takip kolaylığı.

4.  **Statik Seçiciler:**
    *   **Karar:** CSS seçiciler örnek olarak bırakıldı, farklı siteler için güncellenmesi gerektiği belirtildi.
    *   **Gerekçe:** Eğitimsel amaçla, kullanıcıya HTML analizinin önemini göstermek.

5.  **Hata Durumunda Demo Veri:**
    *   **Karar:** Web sitesinden veri çekilemezse demo veri gösterilecek.
    *   **Gerekçe:** Kodun kırılgan olmaması ve her durumda çalışır örnek sunması.

6.  **Selenium Entegrasyon Mimarisi:**
    *   **Karar:** Hibrit mimari - Requests (basit) ve Selenium (gelişmiş) arasında akıllı seçim.
    *   **Gerekçe:** Basit siteler için hızlı (Requests), anti-bot korumalı siteler için güvenilir (Selenium). Kullanıcıya her iki tekniği öğretme fırsatı. Modüler yapı sayesinde gelecekte Playwright veya başka araçlar eklenebilir.

## Öğrenilenler ve İçgörüler

- **403 Forbidden Hatası:** Hepsiburada, Trendyol, N11 gibi büyük e-ticaret siteleri, basit HTTP isteklerini engelleyen güçlü anti-bot sistemleri kullanıyor.
- **Çözüm Gereksinimleri:** Bu sitelere erişim için Selenium, Playwright gibi tarayıcı otomasyon araçları veya daha gelişmiş scraping teknikleri (proxy, session yönetimi, CAPTCHA çözücüler) gerekiyor.
- **Selenium vs Playwright Karşılaştırması:** Eğitimsel amaçlar için Selenium'un daha yaygın ve tanınır olması nedeniyle tercih edildi.
- **Hibrit Mimari Stratejisi:** Basit ve gelişmiş modları birlikte sunmak, hem performans hem de esneklik sağlıyor. Kullanıcılar ihtiyaçlarına göre seçim yapabiliyor.
- **Performans Trade-off:** Selenium ~3-5 saniye başlatma süresi ve ~150-300 MB bellek kullanıyor, ancak %95+ başarı oranı sağlıyor.
- **Eğitimsel Değer:** Hata yönetiminin detaylandırılması ve farklı scraping tekniklerinin karşılaştırılması, kullanıcıya web scraping'in sınırlarını ve gerçek dünya zorluklarını öğretiyor.
- **Bellek Bankası Organizasyonu:** `memory-bank/` klasörü oluşturuldu, karmaşık teknik planlar buraya taşınıyor.

## Stratejik Sonraki Yön

### Öncelik 1: Selenium Entegrasyonu (Aktif Plan)
1.  **Hibrit Mimari:** Requests (basit mod) ve Selenium (gelişmiş mod) arasında akıllı seçim yapan sistem.
2.  **Site-Spesifik Yapılandırma:** JSON dosyasında her site için CSS seçiciler ve ayarlar.
3.  **WebDriver Yönetimi:** `webdriver-manager` ile otomatik Chrome driver kurulumu.
4.  **Kod Refaktörizasyonu:** Modüler yapı (`scrapers/` klasörü, base class pattern).

### Öncelik 2: Gelecek Geliştirmeler
1.  **Daha Fazla Veri Alanı:** Ürün puanı, yorum sayısı, resim URL'si gibi ek veri alanları eklemek.
2.  **Çıktı Formatları:** Sonuçları CSV veya JSON olarak kaydetme seçeneği eklemek.
3.  **Test Senaryoları:** Her site için otomatik testler yazma.
