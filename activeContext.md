
# Aktif Bağlam - Strateji Defteri

## Mevcut Çalışma Odağı
Selenium entegrasyonu ve hibrit mimari için kod ve dokümantasyon güncellemeleri yapıldı. Şu anki odak, kodun modülerleştirilmesi (scrapers/ klasörü, base_scraper.py), Requests ve Selenium modlarının ayrıştırılması, siteye özel yapılandırma ve kullanıcıya mod seçimi sunan bir ana akış oluşturmaktır. Proje, gerçek dünya anti-bot engellerini aşabilen, sürdürülebilir ve genişletilebilir bir araca evrilmektedir.


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
- `selenium_scraper.py` modülü ve `config/sites_config.json` dosyası başarıyla oluşturuldu. Artık hem Requests hem Selenium tabanlı scraping için modüler altyapı hazır.
- Ana `scraper.py` dosyasının hibrit mimariye uygun şekilde güncellenmesi süreci başlatıldı. Kullanıcıdan mod ve site seçimi alan, uygun scraper'ı başlatan factory pattern uygulanacak.

- **Modülerlik ve Sürdürülebilirlik:** Kodun modüllere ayrılması, yeni scraping stratejilerinin ve sitelerin kolayca eklenmesini sağlıyor.
- **Anti-bot Sistemleri:** Büyük e-ticaret siteleri, basit HTTP isteklerini engelleyen güçlü anti-bot sistemleri kullanıyor. Selenium ile gerçek tarayıcı simülasyonu başarı oranını artırıyor.
- **Yapılandırma Yönetimi:** Seçicilerin ve site ayarlarının JSON dosyasına taşınması, kodun sadeleşmesini ve bakımını kolaylaştırıyor.
- **Selenium vs Playwright:** Eğitimsel ve topluluk desteği açısından Selenium tercih edildi, ancak mimari Playwright gibi alternatiflere de açık.
- **Headless ve Otomasyon:** Headless mod ile sunucu ortamlarında da scraping yapılabiliyor.
- **Dokümantasyonun Önemi:** Bellek bankası ve ReadMe güncellemeleri, projenin sürdürülebilirliği için kritik.


## Stratejik Sonraki Yön

### Öncelik 1: Hibrit Mimariyi Tamamlamak (Aktif Plan)
1.  **requests_scraper.py ve selenium_scraper.py**: Kodun iki ayrı modüle taşınması ve base_scraper.py'dan kalıtım alınması.
2.  **config/sites_config.json**: Tüm site seçicilerinin ve ayarlarının JSON dosyasına taşınması.
3.  **scraper.py**: Kullanıcıdan mod ve site seçimi alan, uygun scraper'ı başlatan factory pattern ile güncellenmesi.
4.  **Selenium'da Headless ve WebDriver yönetimi**: Otomatik driver kurulumu ve headless modun test edilmesi.
5.  **ReadMe ve bellek bankası güncellemeleri**: Tüm mimari ve kullanım değişikliklerinin dokümante edilmesi.

### Öncelik 2: Gelecek Geliştirmeler
1.  **Daha Fazla Veri Alanı:** Ürün puanı, yorum sayısı, resim URL'si gibi ek veri alanları eklemek.
2.  **Çıktı Formatları:** Sonuçları CSV veya JSON olarak kaydetme seçeneği eklemek.
3.  **Test Senaryoları:** Her site için otomatik testler yazma.
