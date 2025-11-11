import json
import os
from scrapers.requests_scraper import RequestsScraper
from scrapers.selenium_scraper import SeleniumScraper

# Demo veri fallback
DEMO_PRODUCTS = [
    {"name": "Örnek Ürün 1: Laptop", "price": "15.000 TL"},
    {"name": "Örnek Ürün 2: Akıllı Telefon", "price": "8.000 TL"},
    {"name": "Örnek Ürün 3: Kulaklık", "price": "1.200 TL"},
]

CONFIG_PATH = os.path.join("config", "sites_config.json")

# Kullanıcıya gösterilecek site listesi config'ten alınır

def load_config():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)

def display_products(product_list):
    print("\n" + "="*50)
    if not product_list:
        print("Gösterilecek ürün bulunamadı.")
    else:
        for i, product in enumerate(product_list, 1):
            print(f"{i}. Ürün: {product['name']}")
            print(f"   Fiyat: {product['price']}")
            print("-"*50)


def main():
    config = load_config()
    site_keys = list(config.keys())
    print("🛍️  E-ticaret Ürün Kazıyıcı")
    print("="*50)
    print("Kazıma modu seçin:")
    print("1) Requests (hızlı, temel)")
    print("2) Selenium (gelişmiş, anti-bot)")
    print("Boş bırakılırsa 1 (Requests).")
    mode = input("Mod (1/2): ").strip()
    headless = True
    if mode == "2":
        headless_input = input("Selenium için headless modda çalıştırılsın mı? (E/h): ").strip().lower()
        headless = (headless_input != "h")
        scraper_cls = SeleniumScraper
    else:
        scraper_cls = RequestsScraper
    print("\nHangi siteden ürün bilgisi kazınsın?")
    for idx, key in enumerate(site_keys, 1):
        print(f"{idx}) {key.title()} ({config[key]['url']})")
    print(f"{len(site_keys)+1}) Manuel giriş")
    print(f"Boş bırakılırsa 1 ({site_keys[0].title()}) seçilir.")
    secim = input(f"Seçiminiz (1/{len(site_keys)+1}): ").strip()
    if secim and secim.isdigit() and 1 <= int(secim) <= len(site_keys):
        site_key = site_keys[int(secim)-1]
        site_conf = config[site_key]
        url = site_conf["url"]
        selectors = site_conf["selectors"]
        wait_time = site_conf.get("wait_time", 5)
    elif secim == str(len(site_keys)+1):
        url = input("Lütfen bir e-ticaret ürün listeleme sayfası URL'si girin: ").strip()
        print("Manuel URL için hangi sitenin selectorlarını kullanmak istersiniz?")
        for idx, key in enumerate(site_keys, 1):
            print(f"{idx}) {key.title()} ({config[key]['url']})")
        site_sec = input(f"Seçiminiz (1/{len(site_keys)}): ").strip()
        if site_sec and site_sec.isdigit() and 1 <= int(site_sec) <= len(site_keys):
            site_key = site_keys[int(site_sec)-1]
            site_conf = config[site_key]
            selectors = site_conf["selectors"]
            wait_time = site_conf.get("wait_time", 5)
        else:
            selectors = {}
            wait_time = 5
    else:
        site_key = site_keys[0]
        site_conf = config[site_key]
        url = site_conf["url"]
        selectors = site_conf["selectors"]
        wait_time = site_conf.get("wait_time", 5)
    print(f"\n'{url}' adresinden ürünler çekiliyor...")
    if scraper_cls is SeleniumScraper:
        scraper = scraper_cls(url, selectors, headless=headless, wait_time=wait_time)
    else:
        scraper = scraper_cls(url, selectors)
    html = scraper.fetch()
    products = scraper.parse(html)
    if not products:
        print("\nUyarı: Gerçek veriler çekilemedi. Demo verileri gösteriliyor.")
        products_to_display = DEMO_PRODUCTS
    else:
        products_to_display = products
    display_products(products_to_display)

if __name__ == "__main__":
    main()
