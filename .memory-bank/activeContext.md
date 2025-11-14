# activeContext.md — Aktif Bağlam (Bellek Bankası)

## Amaç
Bu dosya projenin o anki "zihinsel durumu"dur: hangi modüller, hangi sorunlar, hangi kararlar ve nedenleri. Bu bir yapılacaklar listesi değil; kısa ve net bir özet olmalıdır.

## Güncel Durum (14 Nov 2025)
- Proje: CLI'den Streamlit + Plugin mimarisine dönüşüm sürecinde.
- Kök dizin yapısı kullanıcı tarafından Repository `ReadMe.md`'e uygun şekilde oluşturuldu: `core/`, `core/scrapers/`, `custom_plugins/`, `utils/`, `data/` ve `_legacy_backup/` dizinleri mevcut.
- Öncelik: `/.memory-bank/` içindeki dokümantasyon sabitlenmiş ve proje dönüşüm kararları kayıt altına alınmıştır.
- Kod: `custom_plugins/_template.py` ve `custom_plugins/README.md` hazır. Ancak bazı çekirdek dosyalar hâlâ hem kök `scrapers/` içinde hem de `core/scrapers/` içinde bulunuyor; gerçek taşıma (`git mv`) yapılmadı — bu nedenle commit geçmişinin korunması için `git mv` ile taşıma öneriliyor.
- Engeller: Anti-bot korumaları (Cloudflare, CAPTCHA, JS-challenge) bazı hedef sitelerde veri çekmeyi engelliyor; Selenium stratejileri, proxy ve davranış simülasyonu hâlâ araştırılıyor.

## Kararlar (Onay Bekleyen / Onaylanan)
- Onaylanan: Bellek bankası önce güncellenecek; sonra kaynak dosyalar taşınacak.
- Onaylanan: Plugin API basit tutulacak: `metadata` + `run(url, config)` → `List[Dict]`.
- Bekliyor: `custom_plugins` için production sandbox politikası ve manifest zorunlulukları.
- Yeni Not: Repository yapısını kullanıcı oluşturdu; taşıma (fiziksel dosya hareketi) ve commit'leri gerçekleştirmeden önce onay isteniyor.

## Son Eylemler (Kısa)
1. `/.memory-bank/` dosyalarını yeni protokole göre yeniden yaz (tamamlandı).
2. `custom_plugins/_template.py` ve `custom_plugins/README.md` oluşturuldu (kullanıcı/repoda mevcut).
3. `core/` ve `utils/` klasörleri oluşturuldu (kullanıcı tarafından lokal olarak tamamlandı). `scrapers/` içeriğinin `core/scrapers/` altına taşınması (fiziksel `git mv`) hâlâ beklemede — bu adım commit geçmişini korumak için önerilir.
4. Taşıma ve commit öncesi: `git status` ve kısa bir taşıma planı gösterilecek, ardından onayınız alınacak.

## Notlar ve Kanıtlar
- Tüm önemli teknik kararlar ve mimari değişiklikler burada belgelenecek.
- Kod veya yapı değişikliği yapılmadan önce bu dosyada bir onay satırı olması önerilir (ör: "ActiveContext updated and approved by Architect").
- Bu güncelleme: 14 Nov 2025 — Bellek, kullanıcının yeni dosya yapısını oluşturduğunu ve taşınma/adım onayını beklediğini kaydeder.