# E-commerce Product Scraper 🛒

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-active-success.svg)](https://github.com/yourusername/ecommerce-scraper)

Türkçe açıklama için [aşağıya inin](#tr)


## 🌟 About The Project

A modular and educational Python web scraper that extracts product information from e-commerce websites. The project demonstrates both basic (Requests + BeautifulSoup) and advanced (Selenium) web scraping techniques. It is designed with a hybrid architecture for real-world scraping challenges (anti-bot, dynamic content).


### Built With
- [Python](https://www.python.org/)
- [Requests](https://docs.python-requests.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [Selenium](https://www.selenium.dev/)
- [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager)


## 🚀 Features


**Hybrid Scraping Modes**: Choose between fast Requests/BeautifulSoup (simple) or Selenium (advanced, anti-bot)
**Headless Mode for Selenium**: Run Selenium in headless mode (no browser window) by selecting the option at runtime.
**Factory Pattern & Modular Design**: The main script uses a factory pattern to select and instantiate the appropriate scraper module based on user input.
**Product Data Extraction**: Scrapes product names and prices from e-commerce sites
**Modular & Extensible**: Easily add new sites or scraping strategies (see `scrapers/` folder)
**Site-Specific Config**: CSS selectors and settings in `config/sites_config.json`
**Site-Specific Parse Functions**: Each supported site (Hepsiburada, N11, Trendyol) uses a dedicated parse function for robust extraction. Hepsiburada uses advanced JSON-LD parsing for real product data, while N11 and Trendyol use custom selector logic.
**Automatic Selector Management**: The scraper auto-selects the correct site and selectors for manual URLs, reducing user error and improving reliability.
**Debug & Test Output**: Detailed debug prints and saved page sources help troubleshoot selector and anti-bot issues. If scraping fails, demo product data is shown.


**Demo Data Fallback**: If scraping fails due to anti-bot measures or selector issues, demo product data is shown.
**Memory Bank System**: Project context, progress, and design notes are tracked in the `memory-bank/` folder for transparency and maintainability.
## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Steps
1. Clone the repository
```bash
git clone https://github.com/hazarute/ecommerce-scraper.git
cd ecommerce-scraper
```


2. Install required packages
```bash
pip install -r requirements.txt
```


## 💻 Usage

The scraper supports both simple (Requests) and advanced (Selenium) modes. You can select the scraping mode and target site at runtime.

**Run the scraper:**
```bash
python scraper.py
```

**Selenium Headless Mode:**
If you select Selenium mode, you will be prompted:
```
Selenium için headless modda çalıştırılsın mı? (E/h):
```
Press Enter or type 'E' for headless (no browser window), or 'h' to see the browser window.

**How it works:**
1. Prompts you to select scraping mode: Requests (fast, basic) or Selenium (advanced, anti-bot)
2. Prompts you to select a site (Hepsiburada, Trendyol, N11) or enter a custom URL
3. Loads site-specific selectors from `config/sites_config.json` and auto-detects site for manual URLs
4. Uses a dedicated parse function for each site:
   - **Hepsiburada:** Extracts product names and prices from embedded JSON-LD blocks for maximum reliability
   - **N11 & Trendyol:** Uses robust CSS selectors and custom logic for dynamic product cards
5. Debug output and saved page sources help troubleshoot issues; fallback demo data is shown if scraping fails
6. Displays results in a formatted table

**Modular Structure:**
- `scrapers/` folder: Contains `base_scraper.py`, `requests_scraper.py`, `selenium_scraper.py`
- `config/sites_config.json`: Site-specific selectors and settings
- `memory-bank/`: Project context, progress, and design notes

### Example Output
```
🛍️  E-commerce Product Scraper
==================================================
Select scraping mode:
1) Requests (fast, basic)
2) Selenium (advanced, anti-bot)
Default is 1 (Requests).
Mode (1/2): 2

Which site to scrape product info from?
1) Hepsiburada (https://www.hepsiburada.com/)
2) Trendyol (https://www.trendyol.com/)
3) N11 (https://www.n11.com/)
4) Manual entry
Default is 1 (Hepsiburada).
Selection (1/2/3/4): 1
Fetching products from 'https://www.hepsiburada.com/' ...

1. Product: iPhone 14 Pro
   Price: 45.999 ₺
--------------------------------------------------
2. Product: Samsung Galaxy S23
   Price: 32.499 ₺
--------------------------------------------------
...
```

## Demo Video

- https://www.loom.com/share/b032cc8c4a40427485de140f8e9f3d10

## ⚠️ Important Disclaimer

**This project is for educational purposes only.** 
- Always respect website terms of service
- Check robots.txt before scraping any website
- Avoid excessive requests to prevent overloading servers
- The authors are not responsible for any misuse of this code

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

Hazar Üte - hazarute@gmail.com

Project Link: [https://github.com/hazarute/ecommerce-scraper](https://github.com/hazarute/ecommerce-scraper)

## 🙏 Acknowledgments

- [Requests Library](https://docs.python-requests.org/) for simplified HTTP requests
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing
- Inspired by various web scraping tutorials and educational resources

---


# E-ticaret Ürün Kazıyıcı 🛒

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![Lisans: MIT](https://img.shields.io/badge/Lisans-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Durum](https://img.shields.io/badge/durum-aktif-başarılı.svg)](https://github.com/hazarute/ecommerce-scraper)

## 🌟 Proje Hakkında

Modüler ve eğitici bir Python web kazıyıcı. Hem temel (Requests + BeautifulSoup) hem de gelişmiş (Selenium) web kazıma tekniklerini gösterir. Gerçek dünya scraping zorlukları (anti-bot, dinamik içerik) için hibrit mimari ile tasarlanmıştır.

> **Not:** Kod, fabrika (factory) deseniyle çalışır; kullanıcıdan alınan moda göre uygun scraper modülü başlatılır. Bellek bankası (`memory-bank/`), proje ilerlemesi ve mimari kararlar için kullanılır.

### Kullanılan Teknolojiler
- [Python](https://www.python.org/)
- [Requests](https://docs.python-requests.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [Selenium](https://www.selenium.dev/)
- [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager)

## 🚀 Özellikler


**Hibrit Kazıma Modları**: Requests/BeautifulSoup (hızlı, basit) veya Selenium (gelişmiş, anti-bot) seçilebilir
**Headless Mod (Selenium)**: Selenium, istenirse headless (görünmez) modda çalıştırılabilir. Çalıştırırken sorulur.
**Fabrika Deseni & Modüler Yapı**: Ana script, kullanıcıdan alınan moda göre uygun scraper modülünü başlatır.
**Ürün Verisi Çekme**: E-ticaret sitelerinden ürün isimleri ve fiyatları çeker
**Modüler & Genişletilebilir**: Yeni site veya scraping stratejisi kolayca eklenebilir (`scrapers/` klasörü)
**Siteye Özel Ayarlar**: CSS seçiciler ve ayarlar `config/sites_config.json` dosyasında
**Hata Yönetimi**: Detaylı HTTP hata mesajları ve yedek demo veri
**Eğitici Odaklı**: Temiz ve iyi dokümante edilmiş kod
**Siteye Özel Parse Fonksiyonları**: Her desteklenen site (Hepsiburada, N11, Trendyol) için ayrı parse fonksiyonu ile daha sağlam veri çekme. Hepsiburada'da JSON-LD ile gerçek ürün verisi, N11 ve Trendyol'da özel seçici mantığı kullanılır.
**Otomatik Seçici Yönetimi**: Manuel URL girildiğinde scraper doğru siteyi ve seçicileri otomatik seçer, hata riskini azaltır.
**Debug & Test Çıktıları**: Detaylı debug print'ler ve kaydedilen sayfa kaynakları ile anti-bot ve seçici sorunları kolayca analiz edilir. Scraping başarısız olursa demo veri gösterilir.


**Demo Veri Desteği**: Anti-bot veya seçici hatası durumunda demo ürün verisi gösterilir.
**Bellek Bankası Sistemi**: Proje bağlamı, ilerleme ve mimari notlar `memory-bank/` klasöründe tutulur.

### Ön Gereksinimler
- Python 3.6 veya üzeri
- pip (Python paket yükleyici)

### Adımlar
1. Depoyu klonlayın
```bash
git clone https://github.com/hazarute/ecommerce-scraper.git
cd ecommerce-scraper
```

2. Gerekli paketleri yükleyin
```bash
pip install -r requirements.txt
```


## 💻 Kullanım

Kazıyıcı hem basit (Requests) hem de gelişmiş (Selenium) modları destekler. Çalıştırırken mod ve site seçimi yapabilirsiniz.

**Kazıyıcıyı çalıştırın:**
```bash
python scraper.py
```

**Selenium Headless Modu:**
Selenium modu seçerseniz şu şekilde sorulur:
```
Selenium için headless modda çalıştırılsın mı? (E/h):
```
Enter veya 'E' ile headless (görünmez) modda, 'h' ile tarayıcı penceresi açık çalışır.

**Nasıl çalışır?**
1. Kazıma modu sorulur: Requests (hızlı, temel) veya Selenium (gelişmiş, anti-bot)
2. Site seçimi (Hepsiburada, Trendyol, N11) veya manuel URL girişi
3. Siteye özel seçiciler `config/sites_config.json` dosyasından yüklenir ve manuel URL'de site otomatik algılanır
4. Her site için özel parse fonksiyonu kullanılır:
   - **Hepsiburada:** Ürün isimleri ve fiyatları JSON-LD bloklarından çekilir (en güvenilir yöntem)
   - **N11 & Trendyol:** Dinamik ürün kartları için özel CSS seçiciler ve mantık
5. Debug çıktıları ve kaydedilen sayfa kaynakları ile sorunlar kolayca analiz edilir; scraping başarısız olursa demo veri gösterilir
6. Sonuçlar terminalde tablo olarak gösterilir

**Modüler Yapı:**
- `scrapers/` klasörü: `base_scraper.py`, `requests_scraper.py`, `selenium_scraper.py`
- `config/sites_config.json`: Siteye özel seçiciler ve ayarlar
- `memory-bank/`: Proje bağlamı, ilerleme ve mimari notlar

### Örnek Çıktı
```
🛍️  E-ticaret Ürün Kazıyıcı
==================================================
Kazıma modu seçin:
1) Requests (hızlı, temel)
2) Selenium (gelişmiş, anti-bot)
Boş bırakılırsa 1 (Requests).
Mod (1/2): 2

Hangi siteden ürün bilgisi kazınsın?
1) Hepsiburada (https://www.hepsiburada.com/)
2) Trendyol (https://www.trendyol.com/)
3) N11 (https://www.n11.com/)
4) Manuel giriş
Boş bırakılırsa 1 (Hepsiburada) seçilir.
Seçiminiz (1/2/3/4): 1
'https://www.hepsiburada.com/' adresinden ürünler çekiliyor...

1. Ürün: iPhone 14 Pro
   Fiyat: 45.999 ₺
--------------------------------------------------
2. Ürün: Samsung Galaxy S23
   Fiyat: 32.499 ₺
--------------------------------------------------
...
```

## Demo Videosu Linki

- https://www.loom.com/share/b032cc8c4a40427485de140f8e9f3d10

## ⚠️ Önemli Uyarı

**Bu proje sadece eğitim amaçlıdır.**
- Web site kullanım koşullarına her zaman saygı gösterin
- Herhangi bir web sitesini kazımadan önce robots.txt'yi kontrol edin
- Sunucuları aşırı yüklememek için fazla istek göndermekten kaçının
- Yazarlar, bu kodun yanlış kullanımından sorumlu değildir

## 🤝 Katkıda Bulunma

Katkılarınız bekleniyor! Lütfen Pull Request göndermekten çekinmeyin. Büyük değişiklikler için, önce neyi değiştirmek istediğinizi tartışmak için bir issue açın.

1. Projeyi Fork edin
2. Feature Branch oluşturun (`git checkout -b feature/MuhtesemOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Muhtesem bir ozellik ekle'`)
4. Branch'e push layın (`git push origin feature/MuhtesemOzellik`)
5. Pull Request açın

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 📞 İletişim

Hazar Üte - hazarute@gmail.com

Proje Linki: [https://github.com/hazarute/ecommerce-scraper](https://github.com/hazarute/ecommerce-scraper)

## 🙏 Teşekkürler

- [Requests Kütüphanesi](https://docs.python-requests.org/) - basitleştirilmiş HTTP istekleri için
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - HTML ayrıştırma için
- Çeşitli web kazıma eğitimleri ve eğitim kaynaklarından ilham alınmıştır

---