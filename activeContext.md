# Aktif Bağlam - Strateji Defteri

## Mevcut Çalışma Odağı
Modern e-ticaret sitelerinin (Hepsiburada, Trendyol, N11) anti-bot koruma sistemlerini anlamak ve kullanıcıya hataları net bir şekilde açıklayan gelişmiş hata yönetimi sağlamak.

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

## Öğrenilenler ve İçgörüler

- **403 Forbidden Hatası:** Hepsiburada, Trendyol, N11 gibi büyük e-ticaret siteleri, basit HTTP isteklerini engelleyen güçlü anti-bot sistemleri kullanıyor.
- **Çözüm Gereksinimleri:** Bu sitelere erişim için Selenium, Playwright gibi tarayıcı otomasyon araçları veya daha gelişmiş scraping teknikleri (proxy, session yönetimi, CAPTCHA çözücüler) gerekiyor.
- **Eğitimsel Değer:** Hata yönetiminin detaylandırılması, kullanıcıya web scraping'in sınırlarını ve gerçek dünya zorluklarını öğretiyor.
- **Bellek Bankası güncellemeleri:** Yapılan değişikliklerin nedenini ve etkisini netleştirir.

## Stratejik Sonraki Yön

1.  **Yapılandırma Dosyası:** URL ve CSS seçicilerini kod dışına almak.
2.  **Daha Fazla Veri Alanı:** Ürün puanı, yorum sayısı, resim URL'si gibi ek veri alanları eklemek.
3.  **Çıktı Formatları:** Sonuçları CSV veya JSON olarak kaydetme seçeneği eklemek.
