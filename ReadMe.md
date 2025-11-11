# E-commerce Product Scraper 🛒

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-active-success.svg)](https://github.com/yourusername/ecommerce-scraper)

Türkçe açıklama için [aşağıya inin](#tr)

## 🌟 About The Project

A simple and educational Python web scraper that extracts product information from e-commerce websites. This project demonstrates basic web scraping techniques using `requests` and `BeautifulSoup` libraries.

### Built With
- [Python](https://www.python.org/)
- [Requests](https://docs.python-requests.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)

## 🚀 Features

- **Product Data Extraction**: Scrapes product names and prices from e-commerce sites
- **Simple Configuration**: Easy to set up and use
- **Educational Focus**: Clean code structure for learning purposes
- **Error Handling**: Includes fallback demo data when scraping fails
- **Customizable**: Easy to modify for different websites

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Steps
1. Clone the repository
```bash
git clone https://github.com/hazarute/ecommerce-scraper.git
cd ecommerce-scraper
```

2. Install required packages
```bash
pip install -r requirements.txt
```

## 💻 Usage


Run the scraper with a simple command:

```bash
python scraper.py
```

When you run the script, you will be prompted to select from popular e-commerce sites (Hepsiburada, Trendyol, N11) or enter a custom product listing URL. The script will:
1. Connect to the selected e-commerce website
2. Extract the first 5 products' names and prices (if selectors are compatible)
3. Display the results in a formatted table in your terminal

### Example Output
```
🛍️  E-commerce Product Scraper
==================================================
Which site to scrape product info from?
1) Hepsiburada (https://www.hepsiburada.com/)
2) Trendyol (https://www.trendyol.com/)
3) N11 (https://www.n11.com/)
4) Manual entry
Default is 1 (Hepsiburada).
Selection (1/2/3/4): 1
'
https://www.hepsiburada.com/' adresinden ürünler çekiliyor...

1. Product: iPhone 14 Pro
   Price: 45.999 ₺
--------------------------------------------------
2. Product: Samsung Galaxy S23
   Price: 32.499 ₺
--------------------------------------------------
...
```

## ⚠️ Important Disclaimer

**This project is for educational purposes only.** 
- Always respect website terms of service
- Check robots.txt before scraping any website
- Avoid excessive requests to prevent overloading servers
- The authors are not responsible for any misuse of this code

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

Hazar Üte - hazarute@gmail.com

Project Link: [https://github.com/hazarute/ecommerce-scraper](https://github.com/hazarute/ecommerce-scraper)

## 🙏 Acknowledgments

- [Requests Library](https://docs.python-requests.org/) for simplified HTTP requests
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing
- Inspired by various web scraping tutorials and educational resources

---

# E-ticaret Ürün Kazıyıcı 🛒

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![Lisans: MIT](https://img.shields.io/badge/Lisans-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Durum](https://img.shields.io/badge/durum-aktif-başarılı.svg)](https://github.com/kullaniciadiniz/ecommerce-scraper)

## 🌟 Proje Hakkında

E-ticaret web sitelerinden ürün bilgilerini çeken basit ve eğitici bir Python web kazıyıcı. Bu proje, `requests` ve `BeautifulSoup` kütüphaneleri kullanılarak temel web kazıma tekniklerini göstermektedir.

### Kullanılan Teknolojiler
- [Python](https://www.python.org/)
- [Requests](https://docs.python-requests.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)

## 🚀 Özellikler

- **Ürün Verisi Çekme**: E-ticaret sitelerinden ürün isimleri ve fiyatları çeker
- **Basit Kurulum**: Kullanımı ve kurulumu kolay
- **Eğitici Odaklı**: Öğrenme amacıyla temiz kod yapısı
- **Hata Yönetimi**: Kazıma başarısız olursa yedek demo verileri gösterir
- **Özelleştirilebilir**: Farklı web siteleri için kolayca değiştirilebilir

## 📦 Kurulum

### Ön Gereksinimler
- Python 3.6 veya üzeri
- pip (Python paket yükleyici)

### Adımlar
1. Depoyu klonlayın
```bash
git clone https://github.com/hazarute/ecommerce-scraper.git
cd ecommerce-scraper
```

2. Gerekli paketleri yükleyin
```bash
pip install -r requirements.txt
```

## 💻 Kullanım

Kazıyıcıyı basit bir komutla çalıştırın:

```bash
python scraper.py
```

Script şunları yapacaktır:
1. Hedef e-ticaret web sitesine bağlanacak
2. İlk 5 ürünün isim ve fiyatlarını çekecek
3. Sonuçları terminalinizde formatlanmış tablo halinde gösterecek

### Örnek Çıktı
```
🛍️  E-ticaret Ürün Kazıyıcı
==================================================
Hangi siteden ürün bilgisi kazınsın?
1) Hepsiburada (https://www.hepsiburada.com/)
2) Trendyol (https://www.trendyol.com/)
3) N11 (https://www.n11.com/)
4) Manuel giriş
Boş bırakılırsa 1 (Hepsiburada) seçilir.
Seçiminiz (1/2/3/4): 1
'
https://www.hepsiburada.com/' adresinden ürünler çekiliyor...

1. Ürün: iPhone 14 Pro
   Fiyat: 45.999 ₺
--------------------------------------------------
2. Ürün: Samsung Galaxy S23
   Fiyat: 32.499 ₺
--------------------------------------------------
...
```

## ⚠️ Önemli Uyarı

**Bu proje sadece eğitim amaçlıdır.**
- Web site kullanım koşullarına her zaman saygı gösterin
- Herhangi bir web sitesini kazımadan önce robots.txt'yi kontrol edin
- Sunucuları aşırı yüklememek için fazla istek göndermekten kaçının
- Yazarlar, bu kodun yanlış kullanımından sorumlu değildir

## 🤝 Katkıda Bulunma

Katkılarınız bekleniyor! Lütfen Pull Request göndermekten çekinmeyin. Büyük değişiklikler için, önce neyi değiştirmek istediğinizi tartışmak için bir issue açın.

1. Projeyi Fork edin
2. Feature Branch oluşturun (`git checkout -b feature/MuhtesemOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Muhtesem bir ozellik ekle'`)
4. Branch'e push layın (`git push origin feature/MuhtesemOzellik`)
5. Pull Request açın

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 📞 İletişim

Hazar Üte - hazarute@gmail.com

Proje Linki: [https://github.com/hazarute/ecommerce-scraper](https://github.com/hazarute/ecommerce-scraper)

## 🙏 Teşekkürler

- [Requests Kütüphanesi](https://docs.python-requests.org/) - basitleştirilmiş HTTP istekleri için
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - HTML ayrıştırma için
- Çeşitli web kazıma eğitimleri ve eğitim kaynaklarından ilham alınmıştır

---