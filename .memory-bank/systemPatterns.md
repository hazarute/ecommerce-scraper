# systemPatterns.md — Sistem Mimarisi ve Desenler (Bellek Bankası)

## Yüksek Seviye Mimarî Hedef
- Streamlit UI (`app.py`) — kullanıcı etkileşimi, plugin ve site seçimi.
- Core motor (`core/engine.py`) — job orchestration, plugin discovery, export yönetimi.
- Core scrapers (`core/scrapers/`) — `base_scraper.py`, `requests_scraper.py`, `selenium_scraper.py` burada toplanacak.
- `custom_plugins/` — kullanıcıların dinamik scraper eklentilerini koyacağı klasör.
- `utils/` — exporters (CSV/JSON), fileops, helper fonksiyonlar.
- `data/` — page source snapshot'ları ve export arşivleri.

## Örnek Repository Ağaç Yapısı
```
project-root/
├─ app.py
├─ core/
│  ├─ engine.py
│  └─ scrapers/
│     ├─ __init__.py
│     ├─ base_scraper.py
│     ├─ requests_scraper.py
│     └─ selenium_scraper.py
├─ custom_plugins/
│  ├─ _template.py
│  └─ README.md
├─ utils/
│  ├─ exporters.py
│  └─ fileops.py
├─ config/
│  └─ sites_config.json
├─ data/
│  ├─ page_sources/
  │  └─ ...
│  └─ exports/
├─ scripts/
│  └─ legacy_scraper.py
└─ .memory-bank/
   ├─ projectbrief.md
   ├─ productContext.md
   ├─ activeContext.md
   ├─ systemPatterns.md
   ├─ techContext.md
   └─ progress.md
```

## Tasarım Desenleri ve Kurallar
- Strategy Pattern: `BaseScraper` ile farklı scraping stratejileri (requests, selenium) uygulanır.
- Factory Pattern: `ScraperFactory.create(mode, site)` ile uygun scraper instance'ı döndürülür.
- Configuration Pattern: Site-spesifik seçiciler `config/sites_config.json` içinde tutulur.
- Fallback Pattern: İlk önce requests denenir; başarısızsa Selenium'a düşülür.

## Plugin Modeli (Sözleşme)
- Her plugin bir Python modülü olacak ve aşağıdaki unsurları sağlayacak:
  - `metadata` (dict): `name`, `version`, `description`, `supported_sites` (opsiyonel)
  - `def run(url: str, config: dict) -> List[dict]` : çalıştırma fonksiyonu
  - Dönen veri formatı: `List[Dict]` — her dict bir ürün nesnesi olmalı (ör: `{'title':..., 'price':..., 'url':...}`)

## Plugin Discovery Önerisi
- `core.engine` startup'ta `custom_plugins/` klasörünü tarar ve `_template.py` dışındaki `*.py` dosyalarını import eder.
- Security: Production ortamında plugin manifest doğrulaması + container/sandbox önerilir.

## İş Akışı (Job Flow)
1. Kullanıcı Streamlit UI'de site, mode ve URL/konfigürasyon seçer.
2. `core.engine` job oluşturur ve uygun runner'ı (core scraper veya plugin) çağırır.
3. Runner veriyi toplar, parse eder ve `List[Dict]` olarak döndürür.
4. `utils.exporters` ile CSV/JSON oluşturulur; `data/exports/` içine timestamp ile kaydedilir.

## Hata Yönetimi
- Standart hata objesi: `{ 'error': True, 'message': str, 'code': int }`.
- UI dostu mesajlar core engine tarafından hazırlanır; detaylı loglar `logs/` içinde saklanır.