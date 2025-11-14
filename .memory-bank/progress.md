# progress.md — İlerleme Durumu (Bellek Bankası)

## Yapılacaklar (TODO)
- [ ] Anti-bot bypass stratejisini seç (proxy/undetected-chromedriver/API)
- [ ] Seçilen stratejiyi implement et
- [ ] N11/Hepsiburada/Trendyol ile tekrar test (anti-bot bypass sonrası)
- [ ] Unit testler ve linter kurulumu (pytest, flake8)
- [ ] Plugin güvenliği için sandbox/manifest politika taslağı ve testleri

## Bitenler (DONE)
- [X] Plugin mimarisine tam geçiş (core'dan site mantığı kaldırıldı, tüm logic pluginlerde)
- [X] Hepsiburada, Trendyol, N11 plugin dosyaları ve .json configler oluşturuldu
- [X] config/sites_config.json kaldırıldı
- [X] Tüm smoke testler ve arayüz doğrulandı (6/6 PASS)
- [X] Modern UI ve plugin discovery başarıyla çalışıyor
- [X] Generic scraper'lar (requests/selenium) Trendyol plugin mantığıyla güncellendi (JSON-LD + selector fallback, manuel/generic modda da geçerli)

## Hatalar (BUGS)
- [!] `custom_plugins` dinamik importu güvenlik riski taşır — production ortamında sandbox veya izole çalışma önerilir.
- [!] Anti-bot engelleri (Cloudflare, CAPTCHA) bazı sitelerde scraping başarısını etkileyebilir; çözüm için proxy, davranış simülasyonu veya insan müdahalesi gerekebilir.
- [!] Trendyol'da (ve bazı sitelerde) Selenium ile alınan page_source'ta ürünler yok, muhtemelen anti-bot/Cloudflare engeli. (14 Nov 2025)

## Notlar
- Bu dosya projenin “fiziksel durumu”nu gösterir ve 14 Nov 2025 tarihinde güncellenmiştir.