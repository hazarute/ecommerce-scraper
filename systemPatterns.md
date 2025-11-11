## 3. Son Mimari Güncellemeler

- `selenium_scraper.py` ile Selenium tabanlı scraping desteği eklendi.
- Tüm siteye özel seçiciler ve ayarlar config/sites_config.json dosyasına taşındı.
- Requests ve Selenium modülleri, base_scraper.py üzerinden ortak arayüzle çalışıyor.
- Ana akışta kullanıcıdan mod ve site seçimi alınacak, uygun scraper factory pattern ile başlatılacak.

# Sistem Mimarisi ve Desenleri

## 1. Genel Sistem Mimarisi

Proje, başlangıçta tek dosya (scraper.py) ve sabit seçicilerle ilerlerken, artık **hibrit ve modüler mimari**ye evrildi. Kod, scrapers/ klasöründe modüllere ayrıldı; base_scraper.py ile soyut taban sınıf, requests_scraper.py ve selenium_scraper.py ile iki ayrı scraping stratejisi uygulanıyor. Tüm siteye özel seçiciler ve ayarlar config/sites_config.json dosyasına taşınıyor. Ana akış, kullanıcıdan mod ve site seçimi alıp uygun scraper'ı başlatan factory pattern ile yönetilecek.


### Güncel Akış Diyagramı (Hibrit Mimari)

```mermaid
flowchart TD
    A[Başla: python scraper.py] --> B[Kullanıcı Seçimi]
    B --> C{Hangi Mod?}
    
    C -->|Basit| D[RequestsScraper]
    C -->|Selenium| E[SeleniumScraper]
    C -->|Akıllı| F{İlk Requests Dene}
    
    F -->|Başarılı| D
    F -->|403 Hatası| E
    
    D --> G[HTTP GET İsteği]
    E --> H[Chrome WebDriver Başlat]
    
    G --> I{Başarılı?}
    H --> J[Sayfayı Yükle ve Bekle]
    
    I -->|Evet| K[HTML İçeriği Al]
    I -->|Hayır| L[Hata Mesajı]
    
    J --> M[JavaScript Yüklenene Kadar Bekle]
    M --> K
    
    K --> N[BeautifulSoup ile Ayrıştır]
    N --> O[Site Config'den Seçicileri Oku]
    O --> P[Ürün Bilgilerini Çek]
    
    P --> Q[Verileri Terminalde Göster]
    L --> R[Demo Veriler Göster]
    
    Q --> S[Bitir]
    R --> S
```


### Güncel Dosya ve Modül Yapısı

```
E-commerce Product Scraper/
├── scraper.py              # Ana giriş noktası, kullanıcı arayüzü ve mod seçimi
├── scrapers/               # Scraper modülleri
│   ├── __init__.py
│   ├── base_scraper.py     # Soyut taban sınıf
│   ├── requests_scraper.py # Requests tabanlı scraper (mod 1)
│   └── selenium_scraper.py # Selenium tabanlı scraper (mod 2)
├── config/
│   └── sites_config.json   # Siteye özel seçiciler ve ayarlar
├── memory-bank/            # Teknik dokümantasyon ve entegrasyon planları
│   └── selenium_integration_plan.md
├── requirements.txt
├── projectbrief.md
├── activeContext.md
├── systemPatterns.md
├── techContext.md
├── progress.md
```

## 2. Temel Mimari Kararlar

- Kodun modüllere ayrılması (scrapers/), sürdürülebilirlik ve genişletilebilirlik sağlar.
- Tüm siteye özel seçiciler ve ayarlar config/sites_config.json dosyasına taşınır.
- Ana akış, kullanıcıdan mod ve site seçimi alıp uygun scraper'ı başlatan factory pattern ile yönetilir.
- Selenium entegrasyonu ile anti-bot sistemleri aşılabilir, headless mod ve otomatik WebDriver yönetimi desteklenir.
```

## 2. Uygulanan Tasarım Desenleri

Selenium entegrasyonu ile birlikte, proje daha profesyonel yazılım tasarım desenlerini kullanmaya başlıyor:

### Strateji Deseni (Strategy Pattern)
- **Amaç:** Farklı kazıma stratejilerini (Requests vs Selenium) değiştirilebilir kılmak.
- **Uygulama:** 
  - `BaseScraper` soyut sınıfı ortak arayüzü tanımlar.
  - `RequestsScraper` ve `SeleniumScraper` bu arayüzü implement eder.
  - Ana program, runtime'da hangi stratejiyi kullanacağına karar verir.

### Fabrika Deseni (Factory Pattern)
- **Amaç:** Hangi scraper türünün oluşturulacağını merkezi bir noktadan yönetmek.
- **Uygulama:** `ScraperFactory.create(mode, site)` metodu uygun scraper'ı döner.

### Yapılandırma Deseni (Configuration Pattern)
- **Amaç:** Site-spesifik ayarları koddan ayırmak.
- **Uygulama:** `sites_config.json` dosyası her site için CSS seçiciler ve diğer parametreleri tutar.

### Geri Düşme Deseni (Fallback Pattern)
- **Amaç:** Bir yöntem başarısız olduğunda alternatif yola geçmek.
- **Uygulama:** 
  - Akıllı mod: İlk önce Requests, başarısız olursa Selenium.
  - Veri çekme: Gerçek veri çekilemezse demo veri göster.

## 3. Kalıcı Teknik Kararlar

- **Modüler Yapıya Geçiş:** Tek dosyadan (`scraper.py`) çoklu modül yapısına (`scrapers/` klasörü) geçiş yapıldı. Bu, kod organizasyonunu iyileştirir ve yeni scraper türlerinin eklenmesini kolaylaştırır.
- **Bağımlılık Yönetimi:** Yeni bağımlılıklar eklendi (`selenium`, `webdriver-manager`) ancak projenin hafif kalması için gereksiz paketlerden kaçınıldı.
- **Yapılandırma Dosyaları:** Site-spesifik ayarlar (URL, CSS seçiciler) JSON dosyasına taşındı. Bu, kodda değişiklik yapmadan yeni siteler eklemeyi sağlar.
- **Geriye Uyumluluk:** Basit Requests modu korundu. Kullanıcılar hala hafif ve hızlı temel scraping'i kullanabilir.
- **Chrome WebDriver Otomasyonu:** `webdriver-manager` kullanarak driver dosyalarını otomatik indirme ve güncelleme. Kullanıcıdan manuel driver kurulumu istenmez.

## 4. Bileşen Etkileşimleri

Yeni hibrit mimari ile bileşenler arası etkileşim karmaşıklaştı:

### İçsel Etkileşimler (Modüller Arası):
- **`scraper.py` (Main) ↔ `ScraperFactory`:** Kullanıcı seçimine göre uygun scraper instance'ı talep eder.
- **`ScraperFactory` → `RequestsScraper` veya `SeleniumScraper`:** İlgili scraper sınıfını oluşturur.
- **`RequestsScraper` → `requests` kütüphanesi:** HTTP GET istekleri yapar.
- **`SeleniumScraper` → `selenium.webdriver`:** Chrome tarayıcısını kontrol eder.
- **Her Scraper → `BeautifulSoup`:** HTML ayrıştırma için ortak parser.
- **Her Scraper → `sites_config.json`:** CSS seçicileri ve site ayarlarını okur.

### Dışsal Etkileşimler (Sistem Dışı):
- **`RequestsScraper` → Hedef Web Sunucusu:** Basit HTTP isteği.
- **`SeleniumScraper` → Chrome WebDriver → Gerçek Chrome Tarayıcı → Hedef Web Sunucusu:** Tam tarayıcı simülasyonu.
- **Tüm Bileşenler → Terminal/Konsol:** Kullanıcıya çıktıları göster.
- **`webdriver-manager` → ChromeDriver Sunucusu:** Otomatik driver indirme.

### Veri Akışı:
```
Kullanıcı Input → ScraperFactory → [Requests|Selenium]Scraper 
    → Web Sitesi → HTML Response → BeautifulSoup 
    → Config Selectors → Parsed Data → Terminal Output
```
