# E-commerce Product Scraper 🛒

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-active%20development-orange.svg)](https://github.com/hazarute/ecommerce-scraper)

**[Türkçe Açıklama İçin Aşağıya İnin](#tr-e-ticaret-ürün-kazıyıcı-)**

---

## 🌟 About The Project

A **modular, extensible, and production-ready** Python web scraper designed to extract product information from Turkish e-commerce websites. The project demonstrates both basic (Requests + BeautifulSoup) and advanced (Selenium) web scraping techniques within a clean, scalable architecture.

**Current Phase:** Transitioning from CLI-based scraper to **Streamlit UI with Plugin Architecture**.

### Key Goals
- ✅ Educational: Clear, well-documented code for learning web scraping principles
- ✅ Production-Ready: Modular design with factory pattern, strategy pattern, and plugin discovery
- ✅ Flexible: Support for multiple scraping strategies (Requests, Selenium, custom plugins)
- ✅ Extensible: Users can add custom scrapers via `custom_plugins/` without modifying core code
- ✅ Maintainable: Memory Bank system ensures transparent project state and decisions

### Built With
- [Python](https://www.python.org/) 3.8+
- [Streamlit](https://streamlit.io/) — Modern UI framework
- [Requests](https://docs.python-requests.org/) — Lightweight HTTP client
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) — HTML parsing
- [Selenium](https://www.selenium.dev/) — Browser automation for dynamic content
- [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager) — Automatic WebDriver management

---

## 🚀 Features

### Core Features
- **Hybrid Scraping Modes**  
  Choose between lightweight (Requests + BeautifulSoup) for fast, simple sites or Selenium for anti-bot protection and dynamic content.

- **Streamlit Web Interface**  
  Modern UI for site selection, scraping mode configuration, and real-time job monitoring. No CLI needed.

- **Plugin Architecture**  
  Add custom scrapers dynamically via `custom_plugins/` folder. Each plugin follows a simple contract: `metadata` dict + `run(url, config) → List[Dict]`.

- **Site-Specific Configuration**  
  All CSS selectors and site-specific settings centralized in `config/sites_config.json`. Easy to extend for new sites.

- **Site-Specific Parse Functions**  
  - **Hepsiburada:** JSON-LD parsing for maximum reliability
  - **N11 & Trendyol:** Custom CSS selectors and parsing logic optimized per site

- **Automatic Selector Detection**  
  Manual URLs are auto-detected and mapped to the correct site and selectors.

- **Demo Data Fallback**  
  If scraping fails due to anti-bot measures or selector issues, demo product data is displayed for testing.

- **Export Options**  
  Results exported as CSV or JSON with automatic timestamp naming (`site_YYYYMMDD_HHMMSS.json`).

- **Debug Mode**  
  Saved page sources (`data/page_sources/`) and detailed logs for troubleshooting.

- **Memory Bank System**  
  Project context, architectural decisions, and progress tracked in `/.memory-bank/` for transparency and maintainability across sessions.

---

## 📦 Installation

### Prerequisites
- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Git** (for cloning)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/hazarute/ecommerce-scraper.git
   cd ecommerce-scraper
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   streamlit run app.py
   # OR (legacy CLI mode)
   python scraper.py
   ```

---

## 💻 Usage

### **Modern Way: Streamlit UI** (Recommended)
```bash
streamlit run app.py
```
- Open your browser at `http://localhost:8501`
- Select site, scraping mode, and configuration
- View results in real-time
- Export as CSV or JSON

### **Legacy CLI Mode** (Still Supported)
```bash
python scraper.py
```
- Follow the interactive prompts
- Select scraping mode (Requests/Selenium)
- Choose site (Hepsiburada, Trendyol, N11) or enter manual URL
- Results displayed in terminal

### **Selenium Headless Mode**
When Selenium is selected, you'll be prompted:
```
Selenium için headless modda çalıştırılsın mı? (E/h):
```
- Press **Enter** or type **E** for headless (no browser window) — Recommended for servers
- Type **h** to see the browser window during scraping

### How It Works

1. **Mode Selection:** Choose between Requests (fast, basic) or Selenium (advanced, anti-bot)
2. **Site Selection:** Pick from preset sites or enter a custom URL
3. **Auto-Detection:** Site and selectors automatically detected from URL
4. **Data Extraction:** Site-specific parse function extracts product names, prices, URLs
5. **Fallback:** Demo data shown if scraping fails
6. **Export:** Results saved as CSV/JSON with timestamp

### Example Output (Terminal)
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
   URL: https://www.hepsiburada.com/...
--------------------------------------------------
2. Product: Samsung Galaxy S23
   Price: 32.499 ₺
   URL: https://www.hepsiburada.com/...
--------------------------------------------------
```

---

## 📁 Project Structure

```
e-commerce-product-scraper/
├─ app.py                      # Streamlit UI (modern interface)
├─ scraper.py                  # CLI entry point (legacy, maintained)
├─
├─ core/                       # Core scraping engine (under development)
│  ├─ engine.py               # Job orchestration & plugin discovery
│  └─ scrapers/               # Core scraper modules
│     ├─ __init__.py
│     ├─ base_scraper.py      # Abstract base class
│     ├─ requests_scraper.py  # Requests + BeautifulSoup strategy
│     └─ selenium_scraper.py  # Selenium strategy
│
├─ scrapers/                  # Current scraper modules (being migrated to core/)
│  ├─ __init__.py
│  ├─ base_scraper.py
│  ├─ requests_scraper.py
│  └─ selenium_scraper.py
│
├─ custom_plugins/            # User-defined scrapers (plugin architecture)
│  ├─ _template.py           # Example plugin template
│  ├─ README.md              # Plugin development guide
│  └─ [user plugins here]
│
├─ utils/                     # Utility modules (under development)
│  ├─ exporters.py           # CSV/JSON export functions
│  └─ fileops.py             # File operations & management
│
├─ config/
│  └─ sites_config.json      # Site-specific selectors & settings
│
├─ data/
│  ├─ page_sources/          # Saved HTML snapshots (debug)
│  ├─ exports/               # CSV/JSON export output
│  └─ logs/                  # Execution logs
│
├─ scripts/
│  └─ legacy_scraper.py      # Backup of original script (if needed)
│
├─ .memory-bank/             # Project brain (AI-Driven Development)
│  ├─ projectbrief.md        # Project definition & scope
│  ├─ productContext.md      # Why this project exists & target users
│  ├─ activeContext.md       # Current mental state & active decisions
│  ├─ systemPatterns.md      # Architecture & design patterns
│  ├─ techContext.md         # Technology stack & setup
│  └─ progress.md            # Task status & known issues
│
├─ requirements.txt          # Python dependencies
├─ .env.example              # Environment variables template
├─ .gitignore               # Git ignore rules
├─ LICENSE                  # MIT License
└─ README.md               # This file
```

---

## 🔧 Configuration

### Site Configuration (`config/sites_config.json`)
Define CSS selectors and settings for each e-commerce site:

```json
{
  "hepsiburada": {
    "url": "https://www.hepsiburada.com/",
    "selectors": {
      "product_container": "...",
      "product_name": "...",
      "product_price": "..."
    },
    "parse_function": "parse_hepsiburada"
  },
  "trendyol": {
    "url": "https://www.trendyol.com/",
    "selectors": {...},
    "parse_function": "parse_trendyol"
  },
  "n11": {
    "url": "https://www.n11.com/",
    "selectors": {...},
    "parse_function": "parse_n11"
  }
}
```

### Environment Variables (`.env`)
For sensitive data like API keys or proxy settings:
```bash
# .env
PROXY_URL=http://proxy.example.com:8080
API_KEY=your_secret_key_here
DEBUG=True
```

---

## 🧩 Plugin Development

Users can extend the scraper with custom plugins without modifying core code.

### Plugin Template (`custom_plugins/_template.py`)
```python
# metadata: Required
metadata = {
    "name": "My Custom Scraper",
    "version": "1.0.0",
    "description": "Scrapes my custom site",
    "supported_sites": ["mysite.com"],
}

# run function: Required
def run(url: str, config: dict) -> list:
    """
    Args:
        url (str): Target URL to scrape
        config (dict): Configuration dict from UI
    
    Returns:
        list: List of product dictionaries
              [{
                  "title": "...",
                  "price": "...",
                  "url": "...",
                  ...
              }, ...]
    """
    # Your scraping logic here
    results = []
    # ... extract products ...
    return results
```

### Adding a Custom Plugin
1. Copy `custom_plugins/_template.py` to `custom_plugins/my_scraper.py`
2. Implement `metadata` and `run()` function
3. Restart Streamlit UI — plugin auto-discovered and available for selection

---

## 🧪 Testing & Debugging

### Run Streamlit in Debug Mode
```bash
streamlit run app.py --logger.level=debug
```

### Check Saved Page Sources
Failed scrapes save HTML to `data/page_sources/` for analysis:
```bash
ls data/page_sources/
# hepsiburada_20251114_143022.html
# trendyol_20251114_144511.html
```

### Run Unit Tests (when available)
```bash
pytest tests/ -v
```

---

## ⚠️ Important Disclaimer & Ethical Use

**This project is for educational and research purposes only.**

- **Respect Website Terms of Service:** Always review and respect the ToS of any website you scrape
- **Check `robots.txt`:** Before scraping any site, verify that scraping is allowed
- **Rate Limiting:** Avoid excessive requests to prevent overloading servers. Use delays between requests
- **Anti-Bot Measures:** Some sites use Cloudflare, CAPTCHA, or JS-based protection. Selenium + headless mode helps, but may still be blocked
- **Data Privacy:** Do not scrape personal or sensitive user data
- **Liability:** The authors are **not responsible** for misuse of this code or legal consequences arising from scraping activities

---

## 📊 Known Limitations & Risks

### Anti-Bot Protection
Some Turkish e-commerce sites use:
- Cloudflare protection
- CAPTCHA challenges
- JavaScript-based content loading

**Workarounds:** Selenium with headless mode, rotating proxies, request delays, User-Agent rotation

### Plugin Security (Production)
Custom plugins execute arbitrary code. For production:
- ✅ Validate plugin manifest (metadata)
- ✅ Check plugin dependencies
- ✅ Run plugins in isolated containers or sandboxes
- ✅ Code review before deployment

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/ecommerce-scraper.git
   cd ecommerce-scraper
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/YourAmazingFeature
   ```

3. **Make your changes** and commit
   ```bash
   git commit -m "Add YourAmazingFeature"
   ```

4. **Push to the branch**
   ```bash
   git push origin feature/YourAmazingFeature
   ```

5. **Open a Pull Request** on GitHub

For major changes, please open an issue first to discuss your proposal.

---

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 📞 Contact & Support

**Author:** Hazar Üte  
**Email:** hazarute@gmail.com  
**GitHub:** [hazarute](https://github.com/hazarute)  
**Project Link:** [ecommerce-scraper](https://github.com/hazarute/ecommerce-scraper)

---

## 🙏 Acknowledgments & References

- [Requests Library](https://docs.python-requests.org/) — HTTP client
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) — HTML parsing
- [Selenium](https://www.selenium.dev/) — Browser automation
- [Streamlit](https://streamlit.io/) — UI framework
- Web scraping tutorials and educational resources

---

---

# TR: E-ticaret Ürün Kazıyıcı 🛒

[![Python Sürümü](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Lisans: MIT](https://img.shields.io/badge/Lisans-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Durum](https://img.shields.io/badge/durum-aktif%20geli%C5%9Ftirme-orange.svg)](https://github.com/hazarute/ecommerce-scraper)

---

## 🌟 Proje Hakkında

Türkçe e-ticaret sitelerinden ürün bilgisi çekebilen, **modüler, genişletilebilir ve üretim-hazır** bir Python web kazıyıcısıdır. Proje, temel (Requests + BeautifulSoup) ve gelişmiş (Selenium) web kazıma tekniklerini temiz, ölçeklenebilir bir mimari içinde gösterir.

**Şu Anki Faz:** CLI tabanlı kazıyıcıdan **Streamlit UI + Plugin Mimarisine** geçiş yapılıyor.

### Ana Hedefler
- ✅ Eğitici: Web kazıma ilkelerini öğrenmek için açık, iyi belgelenmiş kod
- ✅ Üretim-Hazır: Factory pattern, Strategy pattern ve plugin discovery ile modüler tasarım
- ✅ Esnek: Birden fazla kazıma stratejisi (Requests, Selenium, custom plugin'ler)
- ✅ Genişletilebilir: Kullanıcılar core kodu değiştirmeden `custom_plugins/` klasörüne kendi kazıyıcılarını ekleyebilir
- ✅ Bakımlanabilir: Bellek Bankası sistemi projenin durumunu ve kararlarını şeffaf tutar

### Kullanılan Teknolojiler
- [Python](https://www.python.org/) 3.8+
- [Streamlit](https://streamlit.io/) — Modern UI framework'ü
- [Requests](https://docs.python-requests.org/) — Hafif HTTP istemcisi
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) — HTML ayrıştırması
- [Selenium](https://www.selenium.dev/) — Tarayıcı otomasyonu dinamik içerik için
- [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager) — Otomatik WebDriver yönetimi

---

## 🚀 Özellikler

### Temel Özellikler
- **Hibrit Kazıma Modları**  
  Hızlı, basit siteler için Requests + BeautifulSoup veya anti-bot koruması ve dinamik içerik için Selenium seçin.

- **Streamlit Web Arayüzü**  
  Site seçimi, kazıma modu ayarları ve gerçek zamanlı görev izleme için modern UI. CLI'ye ihtiyaç yok.

- **Plugin Mimarisi**  
  `custom_plugins/` klasörüne dinamik olarak kendi kazıyıcılarınızı ekleyin. Her plugin basit bir sözleşmeyi takip eder: `metadata` dict + `run(url, config) → List[Dict]`.

- **Siteye Özel Yapılandırma**  
  Tüm CSS seçiciler ve siteye özel ayarlar `config/sites_config.json` içinde merkezi yönetilir. Yeni siteler için kolay genişletilir.

- **Siteye Özel Parse Fonksiyonları**  
  - **Hepsiburada:** JSON-LD ayrıştırması maksimum güvenilirlik için
  - **N11 & Trendyol:** Her site için optimize edilmiş CSS seçicileri ve özel parse mantığı

- **Otomatik Seçici Algılaması**  
  Manuel URL'ler otomatik olarak doğru site ve seçicilere eşlenir.

- **Demo Veri Yedekleme**  
  Anti-bot ölçüleri veya seçici hataları nedeniyle kazıma başarısız olursa, demo ürün verisi görüntülenir.

- **Export Seçenekleri**  
  Sonuçlar CSV veya JSON olarak otomatik timestamp adlandırması ile çıkartılır (`site_YYYYMMDD_HHMMSS.json`).

- **Debug Modu**  
  Sorun giderme için kaydedilen sayfa kaynakları (`data/page_sources/`) ve detaylı loglar.

- **Bellek Bankası Sistemi**  
  Proje bağlamı, mimari kararlar ve ilerleme `/.memory-bank/` klasöründe tutulur. Şeffaflık ve oturumlar arası bakımlanabilirlik için tasarlanmış.

---

## 📦 Kurulum

### Ön Gereksinimler
- **Python 3.8 veya üzeri**
- **pip** (Python paket yükleyicisi)
- **Git** (depo klonlamak için)

### Adımlar

1. **Depoyu klonlayın**
   ```bash
   git clone https://github.com/hazarute/ecommerce-scraper.git
   cd ecommerce-scraper
   ```

2. **Sanal ortam oluşturun** (önerilir)
   ```bash
   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Bağımlılıkları yükleyin**
   ```bash
   pip install -r requirements.txt
   ```

4. **Kurulumu doğrulayın**
   ```bash
   streamlit run app.py
   # VEYA (eski CLI modu)
   python scraper.py
   ```

---

## 💻 Kullanım

### **Modern Yol: Streamlit UI** (Önerilir)
```bash
streamlit run app.py
```
- Tarayıcınızda `http://localhost:8501` adresini açın
- Siteyi, kazıma modunu ve yapılandırmayı seçin
- Sonuçları gerçek zamanlı olarak görüntüleyin
- CSV veya JSON olarak dışa aktarın

### **Eski CLI Modu** (Hala Destekleniyor)
```bash
python scraper.py
```
- Etkileşimli istemi izleyin
- Kazıma modunu seçin (Requests/Selenium)
- Siteyi seçin (Hepsiburada, Trendyol, N11) veya manuel URL girin
- Sonuçlar terminalde gösterilir

### **Selenium Headless Modu**
Selenium seçildiğinde şu şekilde sorulur:
```
Selenium için headless modda çalıştırılsın mı? (E/h):
```
- **Enter** basın veya **E** yazın headless (görünmez) mod için — Sunucular için önerilir
- **h** yazın kazıma sırasında tarayıcı penceresini görmek için

### Nasıl Çalışır?

1. **Mod Seçimi:** Requests (hızlı, temel) veya Selenium (gelişmiş, anti-bot) seçin
2. **Site Seçimi:** Önceden ayarlanmış sitelerden biri seçin veya manuel URL girin
3. **Otomatik Algılama:** Site ve seçiciler URL'den otomatik olarak algılanır
4. **Veri Çekme:** Siteye özel parse fonksiyonu ürün adlarını, fiyatlarını, URL'lerini çıkartır
5. **Yedekleme:** Kazıma başarısız olursa demo verisi gösterilir
6. **Export:** Sonuçlar timestamp ile CSV/JSON olarak kaydedilir

### Örnek Çıktı (Terminal)
```
🛍️  E-ticaret Ürün Kazıyıcı
==================================================
Kazıma modu seçin:
1) Requests (hızlı, temel)
2) Selenium (gelişmiş, anti-bot)
Boş bırakılırsa 1 (Requests) seçilir.
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
   URL: https://www.hepsiburada.com/...
--------------------------------------------------
2. Ürün: Samsung Galaxy S23
   Fiyat: 32.499 ₺
   URL: https://www.hepsiburada.com/...
--------------------------------------------------
```

---

## 📁 Proje Yapısı

```
e-commerce-product-scraper/
├─ app.py                      # Streamlit UI (modern arayüz)
├─ scraper.py                  # CLI giriş noktası (eski, hala destekleniyor)
├─
├─ core/                       # Temel kazıma motoru (geliştirme aşamasında)
│  ├─ engine.py               # Görev orkestrasyonu ve plugin discovery
│  └─ scrapers/               # Temel kazıyıcı modülleri
│     ├─ __init__.py
│     ├─ base_scraper.py      # Soyut temel sınıf
│     ├─ requests_scraper.py  # Requests + BeautifulSoup stratejisi
│     └─ selenium_scraper.py  # Selenium stratejisi
│
├─ scrapers/                  # Mevcut kazıyıcı modülleri (core/'e taşınıyor)
│  ├─ __init__.py
│  ├─ base_scraper.py
│  ├─ requests_scraper.py
│  └─ selenium_scraper.py
│
├─ custom_plugins/            # Kullanıcı tanımlı kazıyıcılar (plugin mimarisi)
│  ├─ _template.py           # Örnek plugin şablonu
│  ├─ README.md              # Plugin geliştirme rehberi
│  └─ [kullanıcı plugin'leri burada]
│
├─ utils/                     # Yardımcı modüller (geliştirme aşamasında)
│  ├─ exporters.py           # CSV/JSON export fonksiyonları
│  └─ fileops.py             # Dosya işlemleri ve yönetimi
│
├─ config/
│  └─ sites_config.json      # Siteye özel seçiciler ve ayarlar
│
├─ data/
│  ├─ page_sources/          # Kaydedilen HTML snapshot'ları (debug)
│  ├─ exports/               # CSV/JSON export çıktıları
│  └─ logs/                  # Çalıştırma logları
│
├─ scripts/
│  └─ legacy_scraper.py      # Orijinal scriptin yedek kopyası (gerekirse)
│
├─ .memory-bank/             # Proje beyni (AI-Driven Development)
│  ├─ projectbrief.md        # Proje tanımı ve kapsamı
│  ├─ productContext.md      # Projenin neden var olduğu ve hedef kullanıcılar
│  ├─ activeContext.md       # Mevcut zihinsel durum ve aktif kararlar
│  ├─ systemPatterns.md      # Mimari ve tasarım desenleri
│  ├─ techContext.md         # Teknoloji stack'i ve kurulum
│  └─ progress.md            # Görev durumu ve bilinen sorunlar
│
├─ requirements.txt          # Python bağımlılıkları
├─ .env.example              # Ortam değişkenleri şablonu
├─ .gitignore               # Git ignore kuralları
├─ LICENSE                  # MIT Lisansı
└─ README.md               # Bu dosya
```

---

## 🔧 Yapılandırma

### Site Yapılandırması (`config/sites_config.json`)
Her e-ticaret sitesi için CSS seçiciler ve ayarları tanımlayın:

```json
{
  "hepsiburada": {
    "url": "https://www.hepsiburada.com/",
    "selectors": {
      "product_container": "...",
      "product_name": "...",
      "product_price": "..."
    },
    "parse_function": "parse_hepsiburada"
  },
  "trendyol": {
    "url": "https://www.trendyol.com/",
    "selectors": {...},
    "parse_function": "parse_trendyol"
  },
  "n11": {
    "url": "https://www.n11.com/",
    "selectors": {...},
    "parse_function": "parse_n11"
  }
}
```

### Ortam Değişkenleri (`.env`)
API anahtarları veya proxy ayarları gibi hassas veriler için:
```bash
# .env
PROXY_URL=http://proxy.example.com:8080
API_KEY=gizli_anahtar
DEBUG=True
```

---

## 🧩 Plugin Geliştirme

Kullanıcılar core kodu değiştirmeden custom plugin'ler ile kazıyıcıyı genişletebilir.

### Plugin Şablonu (`custom_plugins/_template.py`)
```python
# metadata: Zorunlu
metadata = {
    "name": "Benim Custom Kazıyıcı",
    "version": "1.0.0",
    "description": "Benim custom sitemi kazır",
    "supported_sites": ["mysite.com"],
}

# run fonksiyonu: Zorunlu
def run(url: str, config: dict) -> list:
    """
    Args:
        url (str): Kazıma yapılacak hedef URL
        config (dict): UI'den gelen yapılandırma dict'i
    
    Returns:
        list: Ürün sözlüklerinin listesi
              [{
                  "title": "...",
                  "price": "...",
                  "url": "...",
                  ...
              }, ...]
    """
    # Kazıma mantığınız burada
    results = []
    # ... ürünleri çıkartın ...
    return results
```

### Custom Plugin Ekleme
1. `custom_plugins/_template.py` dosyasını `custom_plugins/my_scraper.py` olarak kopyalayın
2. `metadata` ve `run()` fonksiyonunu uygulayin
3. Streamlit UI'ı yeniden başlatın — plugin otomatik keşfedilir ve seçilir hale gelir

---

## 🧪 Test Etme ve Debug

### Streamlit Debug Modunda Çalıştırın
```bash
streamlit run app.py --logger.level=debug
```

### Kaydedilen Sayfa Kaynaklarını Kontrol Edin
Başarısız kazımalar HTML'i `data/page_sources/` içine kaydeder:
```bash
ls data/page_sources/
# hepsiburada_20251114_143022.html
# trendyol_20251114_144511.html
```

### Unit Test'leri Çalıştırın (varsa)
```bash
pytest tests/ -v
```

---

## ⚠️ Önemli Uyarı ve Etik Kullanım

**Bu proje sadece eğitim ve araştırma amaçları içindir.**

- **Web Sitesi Hizmet Koşullarına Uyun:** Herhangi bir siteyi kazımadan önce Hizmet Koşulları'nı gözden geçirin ve uyun
- **`robots.txt` Kontrol Edin:** Herhangi bir siteyi kazımadan önce kazımanın izin verilip verilmediğini doğrulayın
- **Hız Sınırlaması:** Sunucuları aşırı yüklememek için aşırı istek göndermekten kaçının. İstekler arasında gecikmeler kullanın
- **Anti-Bot Ölçüleri:** Bazı siteler Cloudflare, CAPTCHA veya JS tabanlı koruma kullanır. Selenium + headless mod yardımcı olur, ancak yine de engellenebilir
- **Veri Gizliliği:** Kişisel veya hassas kullanıcı verilerini kazımayın
- **Sorumluluk:** Yazarlar, bu kodun yanlış kullanımından veya kazıma aktivitelerinden kaynaklanan yasal sonuçlardan **sorumlu değildir**

---

## 📊 Bilinen Sınırlamalar ve Riskler

### Anti-Bot Koruması
Bazı Türkçe e-ticaret siteleri şunları kullanır:
- Cloudflare koruması
- CAPTCHA zorlukları
- JavaScript tabanlı içerik yükleme

**Çözümler:** Selenium headless modu, proxy rotasyonu, istek gecikmeleri, User-Agent rotasyonu

### Plugin Güvenliği (Prodüksiyon)
Custom plugin'ler arbitrer kod çalıştırır. Prodüksiyon için:
- ✅ Plugin manifest'i doğrulayın (metadata)
- ✅ Plugin bağımlılıklarını kontrol edin
- ✅ Plugin'leri izole konteynerler veya sandbox'larda çalıştırın
- ✅ Dağıtımdan önce kod incelemesi yapın

---

## 🤝 Katkıda Bulunma

Katkılarınız memnuniyetle karşılanır! Lütfen şu adımları izleyin:

1. **Depoyu fork edin**
   ```bash
   git clone https://github.com/yourusername/ecommerce-scraper.git
   cd ecommerce-scraper
   ```

2. **Özellik branch'i oluşturun**
   ```bash
   git checkout -b feature/HarikaBirOzellik
   ```

3. **Değişiklikleri yapın ve commit edin**
   ```bash
   git commit -m "HarikaBirOzellik ekle"
   ```

4. **Branch'e push yapın**
   ```bash
   git push origin feature/HarikaBirOzellik
   ```

5. **GitHub'da Pull Request açın**

Büyük değişiklikler için lütfen önce önerinizi tartışmak üzere bir issue açın.

---

## 📝 Lisans

Bu proje **MIT Lisansı** altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 📞 İletişim ve Destek

**Yazar:** Hazar Üte  
**Email:** hazarute@gmail.com  
**GitHub:** [hazarute](https://github.com/hazarute)  
**Proje Linki:** [ecommerce-scraper](https://github.com/hazarute/ecommerce-scraper)

---

## 🙏 Teşekkürler ve Referanslar

- [Requests Kütüphanesi](https://docs.python-requests.org/) — HTTP istemcisi
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) — HTML ayrıştırması
- [Selenium](https://www.selenium.dev/) — Tarayıcı otomasyonu
- [Streamlit](https://streamlit.io/) — UI framework'ü
- Web kazıma eğitimleri ve eğitim kaynakları

---

**Son Güncelleme:** 14 Kasım 2025 | Durum: Aktif Geliştirme (Streamlit Geçişi Devam Ediyor)
