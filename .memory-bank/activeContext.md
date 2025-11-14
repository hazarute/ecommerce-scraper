# activeContext.md — Aktif Bağlam (Bellek Bankası)

## Amaç
Bu dosya projenin o anki "zihinsel durumu"dur: hangi modüller, hangi sorunlar, hangi kararlar ve nedenleri. Bu bir yapılacaklar listesi değil; kısa ve net bir özet olmalıdır.

## Güncel Durum (14 Nov 2025 — N11 Anti-Bot Fix & Mode Auto-Detection)
- **Proje Evresi:** Modern Streamlit UI + Plugin Architecture (OPTION 2) tamamlandı. Şimdi **site-specific anti-bot handling** uygulandı.
- **Fokus:** N11/Hepsiburada/Trendyol gibi anti-bot korumalı siteler otomatik Selenium moduna geçiyor.
- **Son Debug (N11 Sorunu):**
  - ✅ N11 403 Forbidden hatası tespit edildi (requests library bloklaması)
  - ✅ Root cause: N11 Cloudflare/anti-bot koruma → Selenium gerekli
  - ✅ Çözüm: URL'den site algılanıp otomatik Selenium mode seçiliyor
- **Tamamlanan Görevler:**
  - ✅ Plugin template + OPTION 2 mimarisi
  - ✅ Örnek plugin (Amazon) + config JSON
  - ✅ URL auto-detection (site + selectors)
  - ✅ N11/Hepsiburada/Trendyol için Selenium force (Commit: 75a6128)
  - ✅ Debug script (tests/debug_n11.py) oluşturuldu
- **Mevcut Durum:** 
  - Tüm core modüller (`core/`, `custom_plugins/`, `utils/`) stabil
  - `app.py` mode auto-detection ile hazır
  - Sidebar'da algılanan site + mode gösterimi aktif
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
1. N11 sitesi 403 Forbidden hatasından Selenium gereksinimini tespit etti
2. URL'den site auto-detection ve mode override implementasyonu
3. tests/debug_n11.py debug scripti oluşturuldu
4. app.py modeline anti-bot siteler için Selenium force eklendi (Commit: 75a6128)

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
- **14 Nov 2025 (~17:00):** Kategori sayfaları ile konfigürasyon güncellendi
- **14 Nov 2025 (~17:30):** URL'den site auto-detect + selector yükleme (Commit: 62a19ca)
- **14 Nov 2025 (~18:00):** Plugin Selector Architecture (OPTION 2) tamamlandı (Commit: 20b8a82)
- **14 Nov 2025 (~18:45):** N11 anti-bot debugging
  - Problem: N11 URL'den kazıma 403 Forbidden döndürüyor
  - Root cause: N11 requests library'yi blokluyor (anti-bot protection)
  - Solution: URL'den N11 algılanınca otomatik Selenium mode aktifleşiyor
  - Commit: 75a6128 "fix: auto-detect mode for N11/Hepsiburada/Trendyol"
- **Sonraki Test:** Streamlit UI'da N11 URL girildiğinde Selenium ile scrape işleminin başarılı olup olmadığı kontrol edilecek