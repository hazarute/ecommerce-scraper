# Ürün Bağlamı: Neden Bir E-ticaret Kazıyıcı?

## 1. Çözülen Problem

Web kazıma (web scraping), internetten veri toplamanın güçlü bir yoludur, ancak yeni başlayanlar için karmaşık ve korkutucu olabilir. Birçok geliştirici, HTTP istekleri, HTML yapısı, veri ayıklama ve hata yönetimi gibi temel kavramları öğrenirken zorluk yaşar.

Bu proje, bu öğrenme sürecini basitleştirmeyi hedefler. Karmaşık framework'ler veya kurulumlar olmadan, sadece birkaç temel Python kütüphanesi kullanarak web kazımanın temel mantığını adım adım gösteren, çalışan ve anlaşılır bir örnek sunar. Proje, "Bir web sitesinden veri nasıl çekilir?" sorusuna doğrudan ve pratik bir cevap verir.

## 2. Hedef Kitle

- Web kazımaya yeni başlayan Python geliştiricileri.
- `requests` ve `BeautifulSoup` kütüphanelerinin pratik kullanımını görmek isteyen öğrenciler.
- Küçük ve odaklanmış bir proje üzerinden temel yazılım geliştirme prensiplerini (bağımlılık yönetimi, basit hata kontrolü vb.) öğrenmek isteyenler.

## 3. İdeal Kullanıcı Deneyimi

İdeal kullanıcı deneyimi, "minimum çabayla maksimum öğrenme" prensibine dayanır:

1.  **Kolay Kurulum:** Kullanıcı, GitHub deposunu klonladıktan sonra tek bir komutla (`pip install -r requirements.txt`) gerekli tüm bağımlılıkları kurabilmelidir.
2.  **Anında Çalıştırma:** Kullanıcı, `python scraper.py` komutunu çalıştırdığında, terminalde anında anlamlı bir çıktı görmelidir.
3.  **Anlaşılır Çıktı:** Kazınan ürün bilgileri, terminalde temiz ve formatlanmış bir tablo halinde sunulmalıdır. Bu, programın başarılı bir şekilde çalıştığını anında teyit eder.
4.  **Güvenilirlik:** Eğer hedef web sitesi erişilemez veya yapısı değişmiş olursa bile program çökmemelidir. Bunun yerine, kullanıcıya bilgilendirici bir mesaj göstermeli ve önceden tanımlanmış demo verileri sunarak programın çalışma mantığını sergilemeye devam etmelidir.
5.  **Okunabilir Kod:** Kullanıcı, `scraper.py` dosyasını açtığında, kodun amacını, adımlarını ve mantığını kolayca anlayabilmelidir. Yorum satırları ve net isimlendirmeler bu deneyimin kritik bir parçasıdır.
