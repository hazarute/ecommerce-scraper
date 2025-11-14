# projectbrief.md — Proje Özeti (Bellek Bankası)

## Kısa Tanım
E-commerce Product Scraper projesi, e-ticaret sitelerinden ürün verisi toplayabilen, modüler, genişletilebilir ve öğretici bir Python uygulamasıdır. Proje artık CLI'den Streamlit tabanlı bir kullanıcı arayüzüne ve modüler plugin mimarisine doğru evrilmektedir.

## Kapsam ve Hedefler
- Kullanıcıların `app.py` üzerinden scraping job'ları başlatabildiği Streamlit arayüzü.
- `core/` altında güvenilir çekirdek motor (mevcut `scrapers/` taşınacak).
- `custom_plugins/` ile kullanıcıların kendi scraper modüllerini dinamik olarak ekleyebilmesi.
- `utils/` içinde export ve yardımcı fonksiyonların merkezi yönetimi (CSV/JSON, fileops, retry).

## Başarı Kriterleri
- Streamlit UI üzerinden core scraper'lar çalıştırılabiliyor.
- Plugin discovery ve yükleme mekanizması çalışıyor; örnek `_template.py` ile bir plugin eklenebiliyor.
- Bellek bankası (`/.memory-bank/`) tüm mimari kararları, aktivite durumunu ve ilerlemeyi doğru yansıtıyor.

## Dönüşüm Stratejisi (Öncelikler)
1. Önce `/.memory-bank/` dosyaları güncellenecek ve yeni protokole göre sabitlenecek.
2. Bellek bankası onaylandıktan sonra dosya sistemi yeniden düzenlenecek (`core/`, `custom_plugins/`, `utils/`, `data/`).
3. Taşıma işlemleri `git mv` ile yapılacak, commit geçmişi korunacak.

## Roller
- **Ürün Mimarı (Siz):** Hedefleri ve öncelikleri belirler.
- **Geliştirici (Ben / Hazar):** Bellek bankası güncellemesi, dosya taşıma/yeniden düzenleme, şablonların oluşturulması ve gerektiğinde kod üretimi.

---
Bu dosya `/.memory-bank/`'ın anayasasıdır: önemli değişiklikler burada belgelemelidir.