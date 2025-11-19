# activeContext.md — Aktif Bağlam (Bellek Bankası)

## Amaç
Bu dosya projenin o anki "zihinsel durumu"dur: Hangi modüller, hangi sorunlar, hangi kararlar ve nedenleri. TO-DO listesi değildir; kısa ve net bir özet sunar.

## Güncel Durum (19 Nov 2025)
- **Odak:** Akakçe ve diğer pluginlerde Selenium fallback desteği eklendi. Terminal logları detaylandırıldı. Template dosyası güncellendi.
- **Ana Modüller:**
  - Streamlit UI (`app.py`)
  - Core engine (`core/engine.py`)
  - Scraperlar (`core/scrapers/`)
  - Pluginler (`custom_plugins/`)
  - Yardımcılar (`utils/`)
- **Son Testler:**
  - ✅ Akakçe plugin requests ve Selenium fallback ile test edildi.
  - ✅ Template dosyası güncellendi ve terminal logları detaylandırıldı.
  - ✅ Hepsiburada ve diğer pluginler için genel yapı kontrol edildi.
  - ⚠️ Anti-bot engelleri halen geçerli (proxy ve diğer stratejiler için planlama yapılacak).

- ✅ Tüm siteye özel mantık pluginlere taşındı, core generic hale getirildi.
- ✅ Plugin API: `metadata` + `run(url, config)` → `List[Dict]`.
- ✅ Plugin Selector Mimarisi: Ayrı `.json` config dosyası (müşteri dostu).
- ✅ Generic scraper'lar (requests/selenium) artık önce JSON-LD, sonra selector fallback ile çalışıyor (plugin mantığı genel hale getirildi).
- ⏳ Production'da: sandbox politikası + manifest doğrulaması (ileriki iterasyon).

- 19 Nov 2025: Akakçe plugin Selenium fallback desteğiyle güncellendi.
- 19 Nov 2025: Template dosyası terminal logları detaylandırılarak geliştirildi.

## Notlar ve Kanıtlar
  - Test 1: Akakçe plugin requests & Selenium fallback — ✅ PASS
  - Test 2: Template dosyası terminal logları — ✅ PASS
  - Test 3: Hepsiburada plugin kontrolü — ⚠️ Devam eden sorunlar (anti-bot).
  - Akakçe: Selenium fallback başarılı.
  - Hepsiburada: JSON-LD ve fallback testleri devam ediyor.
  - Trendyol: Anti-bot engelleri çözülmedi.
