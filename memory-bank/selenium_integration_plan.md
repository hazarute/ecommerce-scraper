# Selenium Entegrasyon Planı

## Strateji Özeti

Bu belge, projeye Selenium tarayıcı otomasyon kütüphanesinin entegrasyonu için detaylı teknik plan ve mimarisini açıklar. Amaç, anti-bot sistemlerini (Cloudflare, CAPTCHA) aşarak Hepsiburada, Trendyol, N11 gibi modern e-ticaret sitelerinden veri çekebilmektir.

## Selenium vs Playwright Değerlendirmesi

### Selenium Avantajları
- Olgun ve yaygın kullanılan kütüphane
- Geniş topluluk desteği ve dokümantasyon
- Python için iyi entegrasyon (`selenium` paketi)
- Çoklu tarayıcı desteği (Chrome, Firefox, Edge, Safari)
- Eğitimsel amaçlar için tanınırlık

### Playwright Avantajları
- Daha modern ve hızlı
- Yerleşik headless mod optimizasyonu
- Daha iyi asenkron destek
- Daha az kaynak tüketimi

### Karar: Selenium
**Gerekçe:** Proje eğitimsel odaklı olduğu için, daha yaygın ve tanınan Selenium tercih edildi. Kullanıcıların diğer projelerde de karşılaşma olasılığı daha yüksek.

## Mimari Yaklaşım

### Hibrit Strateji: İki Mod Desteği

```
┌─────────────────────────────────────────┐
│         scraper.py (Main)               │
└───────────┬─────────────────────────────┘
            │
            ├─────────────┬───────────────┐
            │             │               │
         Mode 1        Mode 2         Mode 3
      ┌──────────┐  ┌─────────┐   ┌────────┐
      │ Requests │  │Selenium │   │ Hybrid │
      │ (Basit)  │  │(Gelişmiş│   │(Akıllı)│
      └──────────┘  └─────────┘   └────────┘
            │             │               │
            └─────────────┴───────────────┘
                        │
              ┌─────────┴─────────┐
              │  BeautifulSoup    │
              │   (HTML Parser)   │
              └───────────────────┘
```

### Mod 1: Basit Requests (Mevcut)
- Hafif, hızlı, basit siteler için
- Eğitimsel amaçla korunacak

### Mod 2: Selenium (Yeni)
- Anti-bot koruması olan siteler için
- Gerçek tarayıcı simülasyonu
- Daha yavaş ama güvenilir

### Mod 3: Hybrid/Akıllı (Gelecek)
- İlk önce Requests dene
- 403 hatası alırsa otomatik Selenium'a geç

## Teknik Uygulama Planı

### Aşama 1: Bağımlılık Yönetimi
```
requirements.txt güncellemesi:
- selenium
- webdriver-manager (otomatik driver yönetimi için)
```

### Aşama 2: Kod Yapısı Refaktörizasyonu

#### Yeni Dosya Yapısı
```
E-commerce Product Scraper/
├── scraper.py (ana giriş noktası)
├── scrapers/
│   ├── __init__.py
│   ├── base_scraper.py (soyut sınıf)
│   ├── requests_scraper.py (mevcut mantık)
│   └── selenium_scraper.py (yeni)
├── config/
│   └── sites_config.json (site-spesifik seçiciler)
├── requirements.txt
└── README.md
```

### Aşama 3: Site-Spesifik Yapılandırma

`config/sites_config.json` örneği:
```json
{
  "hepsiburada": {
    "url": "https://www.hepsiburada.com/",
    "method": "selenium",
    "selectors": {
      "product_container": "div.product-list",
      "product_item": "li.productListContent-item",
      "product_name": "h3.product-title",
      "product_price": "span.price-value"
    },
    "wait_time": 5
  },
  "trendyol": {
    "url": "https://www.trendyol.com/",
    "method": "selenium",
    "selectors": {...}
  }
}
```

### Aşama 4: Selenium İmplementasyonu

#### selenium_scraper.py Ana Özellikler:
1. **WebDriver Yönetimi:**
   - Chrome WebDriver otomatik kurulum (`webdriver-manager`)
   - Headless mod desteği (UI olmadan çalıştırma)
   - User-Agent ve diğer tarayıcı özelliklerini özelleştirme

2. **Bekleme Stratejileri:**
   - Explicit Wait: Belirli elementlerin yüklenmesini bekle
   - Implicit Wait: Genel sayfa yüklemesi için
   - JavaScript yüklemelerini bekle

3. **Anti-Bot Önlemleri:**
   - Gerçekçi User-Agent kullanımı
   - Viewport ve pencere boyutu ayarları
   - WebDriver tespit engelleyici ayarlar
   - İnsan benzeri davranış (rastgele gecikmeler)

4. **Hata Yönetimi:**
   - TimeoutException yakalama
   - NoSuchElementException yönetimi
   - Screenshot alma (hata durumunda)

### Aşama 5: Kullanıcı Arayüzü Güncellemesi

Konsol menüsüne yeni seçenek:
```
🛍️  E-ticaret Ürün Kazıyıcı
==================================================
Hangi siteden ürün bilgisi kazınsın?
1) Hepsiburada (Selenium - Önerilir)
2) Trendyol (Selenium - Önerilir)
3) N11 (Selenium - Önerilir)
4) Manuel giriş (Basit mod)
5) Manuel giriş (Selenium mod)

Hangi modu kullanmak istersiniz?
[B] Basit mod (hızlı ama kısıtlı)
[S] Selenium mod (yavaş ama güçlü)
[A] Akıllı mod (otomatik seçim) - Varsayılan
```

## Performans ve Kaynak Kullanımı

### Selenium Overhead:
- **Başlatma Süresi:** ~3-5 saniye (Chrome başlatma)
- **Bellek Kullanımı:** ~150-300 MB (Chrome instance)
- **Veri Çekme Süresi:** ~5-10 saniye (sayfa başına)

### Optimizasyonlar:
- Headless mod kullanımı (GUI yok = %30 daha hızlı)
- Gereksiz kaynakları devre dışı bırakma (resimler, CSS)
- WebDriver instance'ı tekrar kullanma (birden fazla URL için)

## Test Stratejisi

### Test Senaryoları:
1. ✅ Hepsiburada ana sayfa ürün çekme
2. ✅ Trendyol kategori sayfası
3. ✅ N11 arama sonuçları
4. ✅ 403 hatası durumunda fallback
5. ✅ Timeout durumunda hata yönetimi
6. ✅ Geçersiz CSS seçicileri durumu

### Manuel Test Checklist:
- [ ] Chrome WebDriver otomatik yükleniyor mu?
- [ ] Headless mod çalışıyor mu?
- [ ] Sayfa tam yüklenene kadar bekliyor mu?
- [ ] Ürün bilgileri doğru çekiliyor mu?
- [ ] Hata durumunda demo veri gösteriliyor mu?

## Eğitimsel Değer

### Kullanıcı Öğrenimleri:
1. **HTTP vs Tarayıcı Otomasyon:** Farkı pratikte görmek
2. **Anti-Bot Sistemleri:** Gerçek dünya korumaları tanımak
3. **Asenkron Yükleme:** JavaScript ile dinamik içerik
4. **Performans Trade-off'ları:** Hız vs güvenilirlik dengesi

## Güvenlik ve Etik

### Uyarılar:
- `robots.txt` dosyalarına saygı gösterilmeli
- Rate limiting uygulanmalı (istekler arası gecikme)
- Kişisel verilerin saklanmaması
- Ticari kullanım için site izinleri gerekli

### README Güncellemesi:
```markdown
⚠️ **Selenium Kullanımı Hakkında:**
Bu proje, eğitim amaçlıdır. Selenium kullanımı, web sitelerinin 
Terms of Service'ini ihlal edebilir. Sorumlu ve yasal kullanım 
sizin sorumluluğunuzdadır.
```

## Gelecek Geliştirmeler

### Faz 2 (İsteğe Bağlı):
- Proxy desteği
- CAPTCHA çözücü entegrasyonu (2captcha API)
- Paralel kazıma (multiple instances)
- Session yönetimi (cookie persistence)
- Veri önbellekleme (cache)

## Sonuç

Bu entegrasyon, projeyi "öğretici örnek"ten "gerçek dünya aracı"na dönüştürecek. Kullanıcılar, modern web scraping'in zorluklarını ve çözümlerini pratikte öğrenecekler.
