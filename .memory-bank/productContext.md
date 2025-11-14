# productContext.md — Ürün Bağlamı (Bellek Bankası)

## Neden (Problem Tanımı)
Proje, web kazıma (web scraping) konusunu öğretmeyi ve belirli e-ticaret sitelerinden yapılandırılmış veri (isim, fiyat, URL, vb.) sağlamayı amaçlıyordu. Proje artık eğitimsel amaçla beraber, üretim-benzeri kullanımı destekleyecek esneklik ve genişletilebilirlik sağlamak üzere yeniden tasarlanıyor.

## Hedef Kitle
- Öğrenciler ve öğreniciler: Temel scraping kavramlarını anlamak isteyenler.
- Geliştiriciler: Kendi site-specific scraperlarını plugin olarak eklemek isteyenler.
- Operasyonel kullanıcılar: UI üzerinden scraping görevleri çalıştırmak, sonuçları gözlemleyip export almak isteyenler.

## Kullanıcı Deneyimi Hedefleri
- **Hızlı geri dönüş:** Streamlit üzerindeki job başlatma kısa süreli sonuç verecek (özet + detay).
- **Şeffaf konfigürasyon:** `config/sites_config.json` ve plugin metadata ile nelerin çalıştığı açıkça görülebilecek.
- **Güvenlik uyarıları:** `custom_plugins` için manifest/meta zorunluluğu olacak; production için sandbox önerilecek.
- **Geriye dönük uyumluluk:** Mevcut CLI `scripts/legacy_scraper.py` olarak kalacak; ana kullanım Streamlit olacak.

## Başarı Ölçütleri
- UI üzerinden en az iki core scraper modu (requests, selenium) çalıştırılabiliyor.
- Kullanıcı `custom_plugins/_template.py` örneğine uyan bir dosya ekleyerek uygulamayı genişletebiliyor.
- Exporters (CSV/JSON) doğru formatta üretiliyor ve `data/exports/` altında arşivleniyor.