# activeContext.md — Aktif Bağlam (Bellek Bankası)

## Amaç
Bu dosya projenin o anki "zihinsel durumu"dur: hangi modüller, hangi sorunlar, hangi kararlar ve nedenleri. Bu bir yapılacaklar listesi değil; kısa ve net bir özet olmalıdır.

## Güncel Durum (14 Nov 2025 — Plugin Architecture v2)
- **Proje Evresi:** Modern Streamlit UI + Bug fixes tamamlandı. Şimdi **plugin selector mimarisi (OPTION 2) uygulandı**.
- **Fokus:** Plugin'ler ayrı `.json` config dosyalarıyla seçici yönetimi yapacaklar.
- **Tamamlanan:**
  - ✅ Plugin template güncelleştirildi (selector yükleme logic)
  - ✅ Örnek plugin: `example_amazon.py` + `example_amazon.json` 
  - ✅ `core/engine.py`: plugin config otomatik yükleme
  - ✅ README.md: müşteri kılavuzu
- **Mevcut Durum:** 
  - `core/`, `custom_plugins/`, `utils/` modülleri stabil ve hazır.
  - `config/sites_config.json` ile site presetleri ve seçiciler mevcut.
  - `utils/exporters.py` ve `utils/fileops.py` fonksiyonel.
  - Mevcut minimal `app.py` daha gelişmiş tasarımla değiştirilecek.
- **Teknik Stack Güncellemesi:** `pandas` (metrikler, veri işleme), `time` (gecikmeler ve loglamalar), mevcut `core.engine` ve `utils` importları korunacak.

 - Yeni Kod Eklentileri (14 Nov 2025):
	 - `utils/fileops.py` eklendi: `save_to_csv` ve `save_html_debug` fonksiyonları eklendi (pandas bağımlılığı eklendi).
	 - `core/engine.py` eklendi: plugin discovery (`discover_plugins`) ve job orchestration (`run_job`) fonksiyonları.
	 - `app.py` eklendi: minimal Streamlit wireframe — mode seçimi, URL girişi, plugin seçimi ve Run butonu ile sonuç gösterimi + CSV export.
	 - `requirements.txt` güncellendi: `streamlit` ve `pandas` eklendi.
   - `utils/exporters.py` eklendi: `export_csv` ve `export_json` fonksiyonları uygulandı.
   - `app.py` güncellendi: `config/sites_config.json` entegrasyonu eklendi (site presetleri ile selectors doldurma).
   - CI: `.github/workflows/ci.yml` eklendi — requirements kurulumu ve temel import smoke testi çalıştırılıyor.

## Kararlar (Onaylanan)
 - ✅ Bellek bankası güncellendi ve taşınma ile ilgili değişiklikler repoya işlendi.
 - ✅ Plugin API: `metadata` + `run(url, config)` → `List[Dict]`.
 - ✅ Plugin Selector Mimarisi: OPTION 2 (Ayrı `.json` config dosyası) seçildi ve uygulandı.
 - ⏳ Production'da: sandbox politikası + manifest doğrulaması (İleriki iterasyon)

## Son Eylemler (Kısa)
1. `/.memory-bank/` dosyaları yeni protokole göre yeniden yazıldı (tamamlandı).
2. `custom_plugins/_template.py` ve `custom_plugins/README.md` oluşturuldu ve repoya eklendi.

## Tasarım Kararları — Plugin Architecture (14 Nov 2025)
- **Seçici Yönetimi:** OPTION 2 (Ayrı .json) ✅
  - Plugin'ler Python kodu + ayrı `.json` config dosyası
  - Seçiciler `.json` dosyasında (müşteri friendly)
  - Selector yükleme sırası: config → .json → default
- **Modulerlik:** Plugin'ler bağımsız, self-contained
- **DRY:** Seçiciler ve kod ayrılı
- **Müşteri Deneyimi:** Müşteri `.json` edit eder, Python yazması gerekmiyor
- **Extensibility:** Yeni plugin = `.py` + `.json` kopyalama + seçicileri güncelleme

## Notlar ve Kanıtlar
- **14 Nov 2025 (~16:30):** Modern UI tasarımı tamamlandı. Smoke test: 6/6 pass ✅
- **14 Nov 2025 (~17:00):** Kategori sayfaları ile konfigürasyon güncellendi (hepsiburada/laptop, n11/laptop, trendyol/laptop)
- **14 Nov 2025 (~17:30):** Selector algılama hatası tespit edildi → **URL'den site AUTO-DETECT** fix uygulandı (62a19ca)
  - Manuel URL girildiğinde, "hepsiburada"/"trendyol"/"n11" içeren linkler otomatik algılanacak
  - Algılanan siteden selector'lar yüklenecek
  - Sidebar'da bilgi mesajı gösterilecek
- **Test Gerekli:** Streamlit'te manuel URL input ve kazıma işlemi doğrulanmalı