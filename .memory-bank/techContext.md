# techContext.md — Teknik Bağlam (Bellek Bankası)

## Stack ve Temel Bağımlılıklar
- **Python:** 3.8+ (3.10/3.11 tavsiye edilir)
- **Core bağımlılıklar:** `requests`, `beautifulsoup4`, `lxml`, `selenium`, `webdriver-manager`, `streamlit`
- **Opsiyonel yardımcılar:** `pydantic` (config validation), `tenacity` (retry), `python-dotenv` (env vars)

## Geliştirme Ortamı (Windows örnek)
1. Sanal ortam oluşturma: `python -m venv .venv`
2. PowerShell (Windows) aktivasyon: `.\.venv\Scripts\Activate.ps1`
3. Bağımlılıkları yükleme: `pip install -r requirements.txt`
4. Streamlit ile çalıştırma: `streamlit run app.py`

## requirements.txt Notları
- `requirements.txt` sadece core bağımlılıklarını içermeli.
- Plugin'lerin özel bağımlılıkları plugin manifest'inde (`metadata['requirements']`) listelenebilir; deployment aşamasında bunlar kontrol edilmelidir.

## Çalıştırma ve Test
- Local UI: `streamlit run app.py`
- Legacy CLI: `python scripts/legacy_scraper.py` (korunuyor ancak ana akış Streamlit olacak)
- Test: `pytest` (varsa) ve linters: `flake8`, `mypy`

## Güvenlik
- `custom_plugins` dinamik import edildiği için production ortamında aşağıdakiler önerilir:
  - Manifest doğrulama (metadata doğruluğu, gereksinimler)
  - Bağımlılıkların denetlenmesi
  - Mümkünse sandbox/container içinde çalıştırma

## Veri ve Arşivleme
- `data/page_sources/` — ham HTML snapshot'lar (debug için)
- `data/exports/` — CSV/JSON çıktılar; dosya isimleri timestamp ile oluşturulmalı: `site_YYYYMMDD_HHMMSS.json`

## DevOps / CI Notları
- CI pipeline: dependency install, flake8, pytest. Streamlit UI entegrasyonu için smoke testler eklenebilir.
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