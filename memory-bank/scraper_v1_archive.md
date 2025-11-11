# scraper.py (İlk Versiyon)

Bu dosya, projenin ilk safhasında kullanılan temel scraper.py kodunu arşivlemek için memory-bank klasörüne taşınmıştır. Kodun tamamı aşağıdadır:

```python
# -*- coding: utf-8 -*-

"""
E-commerce Product Scraper
---
Bu betik, bir e-ticaret web sitesinden ürün bilgilerini (isim ve fiyat)
çekmek için tasarlanmıştır. `requests` kütüphanesi ile web sitesinin HTML
içeriğini alır ve `BeautifulSoup` ile bu içeriği ayrıştırarak istenen
verileri çıkarır.

Eğitim amaçlı olarak hazırlanmıştır ve temel web kazıma prensiplerini
göstermeyi hedefler.

Kullanım:
    python scraper.py
"""

import requests
from bs4 import BeautifulSoup

# --- SABİTLER ---

import sys

# Hedef web sitesinin URL'si.
# Script başlatılırken kullanıcıdan alınacak. Varsayılanlar: Hepsiburada, Trendyol, N11
DEFAULT_SITES = {
    "1": ("Hepsiburada", "https://www.hepsiburada.com/"),
    "2": ("Trendyol", "https://www.trendyol.com/"),
    "3": ("N11", "https://www.n11.com/"),
}

# Tarayıcı taklidi yapmak için HTTP başlıkları. Bazı siteler, otomatik botları
# engellemek için User-Agent kontrolü yapar.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# --- DEMO VERİLERİ ---

# Web sitesine ulaşılamadığında veya veri çekme başarısız olduğunda
# gösterilecek yedek veriler.
DEMO_PRODUCTS = [
    {"name": "Örnek Ürün 1: Laptop", "price": "15.000 TL"},
    {"name": "Örnek Ürün 2: Akıllı Telefon", "price": "8.000 TL"},
    {"name": "Örnek Ürün 3: Kulaklık", "price": "1.200 TL"},
]

# --- ANA FONKSİYONLAR ---

def fetch_page_content(url, headers):
    """
    Verilen URL'ye bir GET isteği gönderir ve sayfanın HTML içeriğini döndürür.

    Args:
        url (str): İstek gönderilecek web sitesi URL'si.
        headers (dict): HTTP isteği için gönderilecek başlıklar.

    Returns:
        str: Sayfanın HTML içeriği. Başarısız olursa None döner.
    """
    try:
        response = requests.get(url, headers=headers, timeout=10)
        # HTTP 200 OK durum kodunu kontrol et
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as e:
        # HTTP hata kodlarına göre özel mesajlar
        status_code = e.response.status_code
        if status_code == 403:
            print(f"\n❌ HATA 403 (Forbidden): Web sitesi erişimi engelledi.")
            print("   Sebep: Site, isteğinizi bot olarak algıladı ve erişimi engelledi.")
            print("   Çözüm: Bu siteler, Cloudflare, CAPTCHA veya diğer anti-bot sistemleri kullanıyor.")
            print("   Not: Basit HTTP istekleri ile bu sitelere erişim mümkün değildir.")
            print("   Alternatif: Selenium gibi tarayıcı otomasyon araçları gerekebilir.")
        elif status_code == 404:
            print(f"\n❌ HATA 404 (Not Found): Sayfa bulunamadı.")
            print("   URL'yi kontrol edin.")
        elif status_code == 429:
            print(f"\n❌ HATA 429 (Too Many Requests): Çok fazla istek gönderildi.")
            print("   Lütfen bir süre bekleyip tekrar deneyin.")
        elif status_code >= 500:
            print(f"\n❌ HATA {status_code} (Server Error): Sunucu hatası.")
            print("   Web sitesinin sunucusunda bir sorun var.")
        else:
            print(f"\n❌ HTTP Hatası {status_code}: {e}")
        return None
    except requests.exceptions.ConnectionError:
        print(f"\n❌ Bağlantı Hatası: İnternet bağlantınızı kontrol edin veya URL geçersiz.")
        return None
    except requests.exceptions.Timeout:
        print(f"\n❌ Zaman Aşımı Hatası: Sunucu 10 saniye içinde yanıt vermedi.")
        return None
    except requests.RequestException as e:
        print(f"\n❌ Beklenmeyen Hata: {type(e).__name__} - {e}")
        return None

def parse_products(html_content):
    """
    HTML içeriğini ayrıştırır ve ürün bilgilerini (isim, fiyat) çıkarır.

    Args:
        html_content (str): Ayrıştırılacak HTML içeriği.

    Returns:
        list: Her biri isim ve fiyat içeren sözlüklerden oluşan bir liste.
              Başarısız olursa boş bir liste döner.
    """
    if not html_content:
        return []

    soup = BeautifulSoup(html_content, "lxml")
    products = []

    # ÖNEMLİ: Aşağıdaki seçiciler, hedef web sitesinin HTML yapısına göre
    # güncellenmelidir. Bu seçiciler sadece birer örnektir.
    # 'product-item' -> her bir ürünün ana kapsayıcısı
    # 'product-title' -> ürün isminin bulunduğu etiket
    # 'product-price' -> fiyatın bulunduğu etiket
    product_elements = soup.select(".product-item")

    for element in product_elements[:5]: # İlk 5 ürünü al
        name_element = element.select_one(".product-title")
        price_element = element.select_one(".product-price")

        if name_element and price_element:
            name = name_element.get_text(strip=True)
            price = price_element.get_text(strip=True)
            products.append({"name": name, "price": price})

    return products

def display_products(product_list):
    """
    Ürün listesini formatlı bir şekilde terminalde gösterir.

    Args:
        product_list (list): Gösterilecek ürünlerin listesi.
    """
    print("\n" + "="*50)
    if not product_list:
        print("Gösterilecek ürün bulunamadı.")
    else:
        for i, product in enumerate(product_list, 1):
            print(f"{i}. Ürün: {product['name']}")
            print(f"   Fiyat: {product['price']}")
            print("-"*50)

# --- ANA PROGRAM AKIŞI ---


def main():
    """
    Ana program fonksiyonu.
    """
    print("🛍️  E-ticaret Ürün Kazıyıcı")
    print("="*50)
    print("Hangi siteden ürün bilgisi kazınsın?")
    for key, (name, url) in DEFAULT_SITES.items():
        print(f"{key}) {name} ({url})")
    print("4) Manuel giriş")
    print("Boş bırakılırsa 1 (Hepsiburada) seçilir.")
    secim = input("Seçiminiz (1/2/3/4): ").strip()
    if secim == "2":
        user_url = DEFAULT_SITES["2"][1]
    elif secim == "3":
        user_url = DEFAULT_SITES["3"][1]
    elif secim == "4":
        user_url = input("Lütfen bir e-ticaret ürün listeleme sayfası URL'si girin: ").strip()
        if not user_url:
            print("Geçerli bir URL girilmedi, varsayılan olarak Hepsiburada seçildi.")
            user_url = DEFAULT_SITES["1"][1]
    else:
        user_url = DEFAULT_SITES["1"][1]
    print(f"\n'{user_url}' adresinden ürünler çekiliyor...")

    html = fetch_page_content(user_url, HEADERS)
    products = parse_products(html)

    if not products:
        print("\nUyarı: Gerçek veriler çekilemedi. Demo verileri gösteriliyor.")
        products_to_display = DEMO_PRODUCTS
    else:
        products_to_display = products

    display_products(products_to_display)


if __name__ == "__main__":
    main()
```
