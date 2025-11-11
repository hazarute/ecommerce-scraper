# Proje Özeti: E-ticaret Ürün Kazıyıcı

## 1. Projenin Tanımı

Bu proje, e-ticaret web sitelerinden ürün bilgilerini (isim ve fiyat) çeken, Python tabanlı basit ve eğitici bir web kazıyıcı uygulamasıdır. Temel amaç, `requests` ve `BeautifulSoup` kütüphaneleri kullanılarak web kazıma tekniklerini anlaşılır bir şekilde göstermektir.

## 2. Projenin Kapsamı

- **Veri Çekme:** Belirlenen bir e-ticaret sitesinden ürün adı ve fiyatı gibi temel verileri çıkarmak.
- **Basit Arayüz:** Çıktıları terminalde formatlanmış bir metin tablosu olarak göstermek.
- **Hata Yönetimi:** Web sitesine ulaşılamaması veya verilerin çekilememesi durumunda, kullanıcıya bir hata mesajı göstermek ve yedek demo verileri sunmak.
- **Eğitimsel Odak:** Kodun temiz, iyi yorumlanmış ve web kazımaya yeni başlayanlar için kolayca anlaşılabilir olmasını sağlamak.

## 3. Temel Gereksinimler

- **Teknoloji:** Python 3.6+ kullanılacak.
- **Kütüphaneler:** `requests` (HTTP istekleri için) ve `BeautifulSoup4` (HTML ayrıştırma için) temel bağımlılıklardır.
- **Çalıştırma:** Proje, `python scraper.py` gibi tek bir komutla çalıştırılabilir olmalıdır.
- **Yapılandırma:** Başlangıçta, kazınacak URL ve HTML seçicileri kod içinde sabit olarak tanımlanacaktır. Gelecekte bu ayarlar bir yapılandırma dosyasından okunabilir hale getirilebilir.
- **Sorumluluk:** Proje, yasal ve etik kurallara uygun şekilde kullanılmalıdır (robots.txt'ye saygı, sunuculara aşırı yüklenmeme vb.). Bu durum `ReadMe.md` dosyasında açıkça belirtilmiştir.
