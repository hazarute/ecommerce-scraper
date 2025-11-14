# activeContext.md — Aktif Bağlam (Bellek Bankası)

## Amaç
Bu dosya projenin o anki "zihinsel durumu"dur: hangi modüller, hangi sorunlar, hangi kararlar ve nedenleri. Bu bir yapılacaklar listesi değil; kısa ve net bir özet olmalıdır.

## Güncel Durum (14 Nov 2025 — Bug Fix & Optimization)
- **Proje Evresi:** v2.0.0 altyapısı + Modern UI tasarımı tamamlandı. Şimdi **selector algılama hatası düzeltiliyor**.
- **Fokus:** Manuel URL girişinde site otomatik algılanmalı, site'e ait selector'lar yüklenebilmeli.
- **Odak Modülü:** `app.py` — URL'den site algılama ve selector yükleme logic'i. `selenium_scraper.py` parse fonksiyonları test edilmeli.
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

## Kararlar (Onay Bekleyen / Onaylanan)
 - Onaylanan: Bellek bankası güncellendi ve taşınma ile ilgili değişiklikler repoya işlendi.
 - Onaylanan: Plugin API basit tutulacak: `metadata` + `run(url, config)` → `List[Dict]`.
 - Bekliyor: `custom_plugins` için production sandbox politikası ve manifest zorunlulukları; dağıtıma alınmadan önce güvenlik incelemesi önerilir.

## Son Eylemler (Kısa)
1. `/.memory-bank/` dosyaları yeni protokole göre yeniden yazıldı (tamamlandı).
2. `custom_plugins/_template.py` ve `custom_plugins/README.md` oluşturuldu ve repoya eklendi.

## Tasarım Kararları ve Bug Fix'ler (14 Nov 2025)
- **Sekmeli Yapı:** 3 tab (Kazıma, Eklenti, Veri Geçmişi) ✅
- **Sidebar Organizasyonu:** Site + Mode, expander'da gelişmiş ayarlar ✅
- **Session State:** Kazıma sonuçları kalıcı ✅
- **Feedback Loop:** Status spinner + toast/balloons ✅
- **AUTO-DETECT:** Manuel URL girişinde "hepsiburada", "trendyol", "n11" içeren linkler otomatik algılanacak ve selector'lar yüklenecek — **BUG FIX** (Commit: 62a19ca)
- **Site Bildirimi:** Manuel input'ta site algılanırsa sidebar'da bilgi mesajı gösterilecek

## Notlar ve Kanıtlar
- **14 Nov 2025 (~16:30):** Modern UI tasarımı tamamlandı. Smoke test: 6/6 pass ✅
- **14 Nov 2025 (~17:00):** Kategori sayfaları ile konfigürasyon güncellendi (hepsiburada/laptop, n11/laptop, trendyol/laptop)
- **14 Nov 2025 (~17:30):** Selector algılama hatası tespit edildi → **URL'den site AUTO-DETECT** fix uygulandı (62a19ca)
  - Manuel URL girildiğinde, "hepsiburada"/"trendyol"/"n11" içeren linkler otomatik algılanacak
  - Algılanan siteden selector'lar yüklenecek
  - Sidebar'da bilgi mesajı gösterilecek
- **Test Gerekli:** Streamlit'te manuel URL input ve kazıma işlemi doğrulanmalı