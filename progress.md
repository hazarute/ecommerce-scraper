# İlerleme Durumu - Görev Panosu



## Yapılacaklar (TO-DO)

- `[ ]` Selenium veya Playwright gibi tarayıcı otomasyon araçlarını araştır ve entegre et (anti-bot sistemlerini aşmak için).
- `[ ]` Farklı e-ticaret siteleri için spesifik CSS seçicilerini tanımla ve yapılandırma dosyasına taşı.

## Tamamlananlar (DONE)

- `[X]` Proje hedeflerini ve kurallarını anlamak için `ReadMe.md` ve `Rules_MemoryBank.md` dosyaları incelendi.
- `[X]` `projectbrief.md` oluşturuldu.
- `[X]` `productContext.md` oluşturuldu.
- `[X]` `activeContext.md` oluşturuldu.
- `[X]` `systemPatterns.md` oluşturuldu.
- `[X]` `techContext.md` oluşturuldu.
- `[X]` `progress.md` (bu dosya) oluşturuldu ve ilk görevler eklendi.
- `[X]` Proje için temel dizin yapısı oluşturuldu.
- `[X]` `requirements.txt` dosyası oluşturuldu.
- `[X]` Temel `scraper.py` dosyası oluşturuldu.
- `[X]` `scraper.py` içine hedef URL ve HTTP başlıkları (User-Agent) için sabitler eklendi.
- `[X]` Web sitesinden HTML içeriğini çeken fonksiyon yazıldı.
- `[X]` HTML içeriğini ayrıştıran ve ürünleri (isim ve fiyat) çıkaran fonksiyon yazıldı.
- `[X]` Çıkarılan verileri terminalde formatlı bir şekilde yazdıran fonksiyon oluşturuldu.
- `[X]` Veri çekme başarısız olduğunda kullanılacak demo veriler tanımlandı.
- `[X]` Ana program akışı (main block) oluşturularak tüm fonksiyonlar bir araya getirildi.
- `[X]` Hepsiburada, Trendyol, N11 sitelerini varsayılan olarak öneren ve manuel girişe izin veren kullanıcı arayüzü eklendi.
- `[X]` Bellek bankası ve ReadMe güncellemeleri yapıldı.
- `[X]` HTTP hata kodlarına göre detaylı ve açıklayıcı hata mesajları eklendi (403, 404, 429, 5xx, timeout, connection error).

## Bilinen Sorunlar (BUGS)

- `[!]` **403 Forbidden Hatası:** Hepsiburada, Trendyol, N11 gibi siteler anti-bot koruması kullanıyor. Basit HTTP istekleri engellenebilir. Selenium/Playwright gibi araçlar gerekebilir.
