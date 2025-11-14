# activeContext.md — Aktif Bağlam (Bellek Bankası)

## Amaç
Bu dosya projenin o anki "zihinsel durumu"dur: hangi modüller, hangi sorunlar, hangi kararlar ve nedenleri. Bu bir yapılacaklar listesi değil; kısa ve net bir özet olmalıdır.

## Güncel Durum (14 Nov 2025)
- Proje: CLI'den Streamlit + Plugin mimarisine dönüşüm başarıyla tamamlandı ve `v2.0.0` sürümü olarak yayımlandı.
- Kök dizin yapısı repoda `ReadMe.md`'de tanımlandığı şekilde düzenlendi: `core/`, `core/scrapers/`, `custom_plugins/`, `utils/`, `data/` ve `_legacy_backup/` dizinleri mevcut.
- Kod: `core/scrapers/` altında `base_scraper.py`, `requests_scraper.py`, `selenium_scraper.py` oluşturuldu (legacy içerik modernize edilerek taşındı). `custom_plugins/_template.py` ve `custom_plugins/README.md` eklendi.
- Release ve VCS: Tüm değişiklikler commit edilip `main` dalına pushlandı; ayrıca `v2.0.0` annotated tag oluşturuldu ve origin'a gönderildi.
- Bağımlılıklar: `requirements.txt` güncellendi; `streamlit` eklendi.
- Engeller: Anti-bot korumaları (Cloudflare, CAPTCHA, JS-challenge) hâlâ bazı sitelerde sorun yaratabiliyor; plugin güvenliği production için ayrı önlem gerektiriyor (sandbox, manifest kontrolü).

 - Yeni Kod Eklentileri (14 Nov 2025):
	 - `utils/fileops.py` eklendi: `save_to_csv` ve `save_html_debug` fonksiyonları eklendi (pandas bağımlılığı eklendi).
	 - `core/engine.py` eklendi: plugin discovery (`discover_plugins`) ve job orchestration (`run_job`) fonksiyonları.
	 - `app.py` eklendi: minimal Streamlit wireframe — mode seçimi, URL girişi, plugin seçimi ve Run butonu ile sonuç gösterimi + CSV export.
	 - `requirements.txt` güncellendi: `streamlit` ve `pandas` eklendi.

## Kararlar (Onay Bekleyen / Onaylanan)
 - Onaylanan: Bellek bankası güncellendi ve taşınma ile ilgili değişiklikler repoya işlendi.
 - Onaylanan: Plugin API basit tutulacak: `metadata` + `run(url, config)` → `List[Dict]`.
 - Bekliyor: `custom_plugins` için production sandbox politikası ve manifest zorunlulukları; dağıtıma alınmadan önce güvenlik incelemesi önerilir.

## Son Eylemler (Kısa)
1. `/.memory-bank/` dosyaları yeni protokole göre yeniden yazıldı (tamamlandı).
2. `custom_plugins/_template.py` ve `custom_plugins/README.md` oluşturuldu ve repoya eklendi.

## Notlar ve Kanıtlar
- Tüm önemli teknik kararlar ve mimari değişiklikler burada belgelenecek.
- Kod veya yapı değişikliği yapılmadan önce bu dosyada bir onay satırı olması önerilir (ör: "ActiveContext updated and approved by Architect").
- Bu güncelleme: 14 Nov 2025 — Bellek, kullanıcının yeni dosya yapısını oluşturduğunu ve taşınma/adım onayını beklediğini kaydeder.