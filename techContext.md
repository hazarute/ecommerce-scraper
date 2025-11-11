## 4. Son Teknik Güncellemeler

- `selenium_scraper.py` ile Selenium tabanlı scraping desteği eklendi.
- Tüm siteye özel seçiciler config/sites_config.json dosyasına taşındı.
- Kodun modüler yapısı sayesinde yeni scraping stratejileri kolayca eklenebilir.

# Teknik Detaylar

## 1. Teknolojiler ve Sürümler

- **Programlama Dili:** Python (Sürüm 3.6 veya üzeri)
- **Temel Kütüphaneler:**
  - `requests`: HTTP istekleri (basit scraping için)
  - `beautifulsoup4`: HTML ayrıştırma
  - `lxml`: BeautifulSoup için hızlı parser
- **Tarayıcı Otomasyon Kütüphaneleri:**
  - `selenium`: Gelişmiş scraping ve anti-bot korumalı siteler için
  - `webdriver-manager`: Chrome WebDriver'ı otomatik indirir ve yönetir
- **Modüler Yapı:**
  - Kod scrapers/ klasöründe modüllere ayrılmıştır (base_scraper.py, requests_scraper.py, selenium_scraper.py)
- **Yapılandırma:**
  - Tüm siteye özel seçiciler ve ayarlar config/sites_config.json dosyasındadır


## 2. Geliştirme Ortamı Kurulumu

1.  **Python Kurulumu:**
  - Python 3.6 veya üzeri gereklidir.
  - Kontrol: `python --version`

2.  **Proje Klonlama:**
  - `git clone https://github.com/hazarute/ecommerce-scraper.git`
  - `cd ecommerce-scraper`

3.  **Sanal Ortam (Önerilir):**
  - `python -m venv venv`
  - Windows: `.\venv\Scripts\activate`
  - macOS/Linux: `source venv/bin/activate`

4.  **Bağımlılıkların Yüklenmesi:**
  - `pip install -r requirements.txt`


## 3. Bağımlılık Yönetimi ve Teknik Notlar

- Tüm bağımlılıklar requirements.txt dosyasındadır:
  - requests
  - beautifulsoup4
  - lxml
  - selenium
  - webdriver-manager

- **Selenium Kurulum Notları:**
    - Google Chrome yüklü olmalı
    - WebDriver otomatik yönetilir (manuel indirme gerekmez)
    - Headless mod ile tarayıcı arayüzü olmadan scraping yapılabilir

## 4. Projeyi Çalıştırma

- Kurulum tamamlandıktan ve (varsa) sanal ortam etkinleştirildikten sonra, kazıyıcıyı çalıştırmak için aşağıdaki komutu kullanın:
  ```bash
  python scraper.py
  ```

## 5. Teknik Kısıtlamalar ve Bilinen Sınırlar

### Requests Modu (Basit):
- **JavaScript Oluşturulan İçerik:** Bu mod, yalnızca sunucudan gelen ilk HTML yanıtını işleyebilir. Eğer bir web sitesi ürün bilgilerini JavaScript kullanarak sonradan yüklüyorsa (dinamik içerik), bu mod o verileri göremez.
- **Anti-Bot Engelleri:** Cloudflare, CAPTCHA veya diğer bot koruma sistemlerine karşı savunmasızdır. 403 Forbidden hataları alınabilir.

### Selenium Modu (Gelişmiş):
- **Performans:** Basit requests moduna göre ~5-10 kat daha yavaştır. Tarayıcı başlatma ve sayfa yükleme süresi ekler.
- **Kaynak Kullanımı:** ~150-300 MB RAM ve CPU kullanımı. Birden fazla paralel instance için kaynak talebi artar.
- **Chrome Bağımlılığı:** Sistemde Google Chrome yüklü olmalıdır. Farklı tarayıcılar için kod değişikliği gerekir.
- **CAPTCHA:** Otomatik CAPTCHA çözme yetenği yoktur. İnsan müdahalesi veya ücretli API servisleri (2captcha) gerekebilir.

### Genel Sınırlamalar:
- **Hız Sınırlamaları (Rate Limiting):** Sunucuyu aşırı yüklememek için istekler arasında gecikme eklenmemiştir. Yüksek frekanslı kullanım IP engeline yol açabilir.
- **Yasal ve Etik:** Web sitelerinin Terms of Service'i kazımayı yasaklayabilir. Kullanıcılar yasal sorumluluğu üstlenmelidir.
- **robots.txt Uyumu:** Program, robots.txt dosyalarını otomatik kontrol etmez. Kullanıcı manuel olarak kontrol etmelidir.
