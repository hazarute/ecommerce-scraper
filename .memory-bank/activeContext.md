# activeContext.md — Aktif Bağlam (Bellek Bankası)

## Amaç
Bu dosya projenin o anki "zihinsel durumu"dur: hangi modüller, hangi sorunlar, hangi kararlar ve nedenleri. Bu bir yapılacaklar listesi değil; kısa ve net bir özet olmalıdır.

## Güncel Durum (14 Nov 2025 — N11 Anti-Bot Testing Complete)
- **Proje Evresi:** Modern Streamlit UI + Plugin Architecture tamamlandı. **Mode auto-detection başarılı, fakat anti-bot koruma test sınırlaması.**
- **Test Sonucu:** 
  - ✅ URL detection başarılı (N11/Hepsiburada otomatik algılanıyor)
  - ✅ Mode override çalışıyor (Selenium moduna geçiliyor)
  - ❌ Cloudflare bot detection tüm siteleri blokluyor
- **Root Cause:** N11, Hepsiburada vb. e-commerce siteleri anti-bot koruma (Cloudflare, etc.) kullanıyor
- **Solution Path:**
  1. Proxy + residential IP (production için)
  2. Undetected-chromedriver (quick fix)
  3. Official API (ideal long-term)
- **Mevcut Durum:** 
  - URL detection fully functional
  - Mode auto-override fully functional
  - Scraping blocked by Cloudflare (expected behavior for bot protection)
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
1. Integration test yaz (N11 + Hepsiburada)
2. URL detection & mode override testi: ✅ PASS
3. Scraping test: ❌ FAIL (Cloudflare blocking)
4. Root cause tespit: Anti-bot koruma tüm sitelerde aktif
5. Test raporu oluştur: TEST_REPORT_N11.md
6. Git commit: e80aedb (test files + report)

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
- **14 Nov 2025 (~18:45):** N11 anti-bot debugging + mode auto-detection (Commit: 75a6128)
- **14 Nov 2025 (~19:00):** URL detection logic verification ✅
- **14 Nov 2025 (~19:15):** Integration tests created (N11, Hepsiburada)
  - Test 1: URL detection & mode override — ✅ PASS
  - Test 2: N11 scraping — ❌ FAIL (Cloudflare blocking)
  - Test 3: Hepsiburada scraping — ❌ FAIL (404 redirect)
- **14 Nov 2025 (~19:30):** Test report created (TEST_REPORT_N11.md)
- **Finding:** All major e-commerce sites have anti-bot protection
  - N11: Cloudflare
  - Hepsiburada: Session/redirect blocking
  - Trendyol: Unknown (not tested yet)
- **Next Action:** Implement proxy or undetected-chromedriver for Cloudflare bypass