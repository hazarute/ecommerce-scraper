# activeContext.md — Aktif Bağlam (Bellek Bankası)

## Amaç
Bu dosya projenin o anki "zihinsel durumu"dur: Hangi modüller, hangi sorunlar, hangi kararlar ve nedenleri. TO-DO listesi değildir; kısa ve net bir özet sunar.

## Güncel Durum (14 Nov 2025)
- **Odak:** Generic scraper'lar (requests/selenium) Trendyol plugin mantığıyla güncellendi: Önce JSON-LD, sonra selector fallback. Manuel/generic modda modern sitelerden veri çekme şansı artırıldı. Trendyol'da halen anti-bot/Cloudflare engeli var, veri çekilemiyor.
- **Ana Modüller:**
  - Streamlit UI (`app.py`)
  - Core engine (`core/engine.py`)
  - Scraperlar (`core/scrapers/`)
  - Pluginler (`custom_plugins/`)
  - Yardımcılar (`utils/`)
- **Son Testler:**
  - ✅ Plugin discovery ve yükleme başarılı
  - ✅ Tüm smoke testler geçti (6/6)
  - ✅ Streamlit arayüzü sorunsuz açıldı
  - ✅ Hepsiburada, Trendyol, N11 için pluginler ve .json configler oluşturuldu
  - ⚠️ Cloudflare/anti-bot engelleri halen geçerli (production için çözüm gerekecek)

- ✅ Tüm siteye özel mantık pluginlere taşındı, core generic hale getirildi.
- ✅ Plugin API: `metadata` + `run(url, config)` → `List[Dict]`.
- ✅ Plugin Selector Mimarisi: Ayrı `.json` config dosyası (müşteri dostu)
- ✅ Generic scraper'lar (requests/selenium) artık önce JSON-LD, sonra selector fallback ile çalışıyor (plugin mantığı genel hale getirildi).
- ⏳ Production'da: sandbox politikası + manifest doğrulaması (ileriki iterasyon)

- 14 Nov 2025: Plugin mimarisi, testler ve arayüz başarıyla doğrulandı.
- 14 Nov 2025: config/sites_config.json kaldırıldı, tüm logic pluginlerde.
  - Seçiciler `.json` dosyasında (müşteri friendly)
  - Selector yükleme sırası: config → .json → default
- 14 Nov 2025: Generic scraper'lar Trendyol plugin mantığıyla güncellendi (JSON-LD + selector fallback). Trendyol'da veri halen çekilemiyor, sayfa kaynağı anti-bot nedeniyle boş veya eksik geliyor.

## Notlar ve Kanıtlar
  - Test 1: URL detection & mode override — ✅ PASS
  - Test 2: N11 scraping — ❌ FAIL (Cloudflare blocking)
  - Test 3: Hepsiburada scraping — ❌ FAIL (404 redirect)
  - N11: Cloudflare
  - Hepsiburada: Session/redirect blocking
  - Trendyol: Unknown (not tested yet)
