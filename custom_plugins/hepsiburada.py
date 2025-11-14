"""
Hepsiburada ürün kazıyıcı plugin

Sayfa kaynağındaki application/ld+json scriptlerinden ürün verisi çeker.
"""

import json
import requests
from bs4 import BeautifulSoup
from pathlib import Path

# Selenium fallback için
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    webdriver = None

metadata = {
    "name": "hepsiburada_plugin",
    "version": "1.0.0",
    "description": "Hepsiburada ürün kazıyıcı — JSON-LD öncelikli.",
    "supported_sites": ["hepsiburada.com"],
    "requirements": ["requests", "beautifulsoup4", "lxml"],
    "default_selectors": {
        "product_item": "article.horizontalProductCard-module_article__mzi-M",
        "product_name": "json-ld",
        "product_price": "json-ld"
    }
}

def _load_selectors_from_json() -> dict:
    current_file = Path(__file__)
    config_file = current_file.parent / f"{current_file.stem}.json"
    if config_file.exists():
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return config.get("selectors", {})
        except Exception:
            pass
    return metadata.get("default_selectors", {})

def run(url: str, config: dict) -> list:
    selectors = config.get('selectors') or _load_selectors_from_json()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    # Önce requests ile dene
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        html = resp.text
    except Exception as e:
        print(f"[hepsiburada_plugin] HTTP Hatası: {e}")
        html = None

    products = []
    if html:
        soup = BeautifulSoup(html, "lxml")
        # Önce JSON-LD ile dene
        json_ld_tags = soup.find_all('script', type='application/ld+json')
        for tag in json_ld_tags:
            try:
                data = json.loads(tag.string)
            except Exception:
                continue
            if isinstance(data, dict) and data.get('@type') == 'ItemList' and 'itemListElement' in data:
                items = data.get('itemListElement', [])
                for item in items:
                    prod = item.get('item', {})
                    name = prod.get('name', 'YOK')
                    offers = prod.get('offers', {})
                    price = offers.get('price', 'YOK')
                    if name and price:
                        products.append({"name": name, "price": price})
                if products:
                    return products
        # Eğer JSON-LD ile bulunamazsa, klasik HTML parse ile dene
        product_item_sel = selectors.get('product_item')
        name_sel = selectors.get('product_name')
        price_sel = selectors.get('product_price')
        if product_item_sel:
            items = soup.select(product_item_sel)
            for el in items:
                name = el.get_text(strip=True)
                price = None
                # Fiyatı bulmak için alt elemanları dene
                price_tag = el.find('div', class_='moria-ProductCard-module_price__')
                if price_tag:
                    price = price_tag.get_text(strip=True)
                if name:
                    products.append({"name": name, "price": price or "YOK"})
            if products:
                return products

    # Eğer requests ile veri bulunamazsa Selenium ile dene
    if webdriver is not None:
        try:
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--window-size=1920,1080')
            options.add_argument(f'user-agent={headers["User-Agent"]}')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.get(url)
            import time as _t; _t.sleep(3)
            html = driver.page_source
            driver.quit()
            soup = BeautifulSoup(html, "lxml")
            # Yine JSON-LD ile dene
            json_ld_tags = soup.find_all('script', type='application/ld+json')
            for tag in json_ld_tags:
                try:
                    data = json.loads(tag.string)
                except Exception:
                    continue
                if isinstance(data, dict) and data.get('@type') == 'ItemList' and 'itemListElement' in data:
                    items = data.get('itemListElement', [])
                    for item in items:
                        prod = item.get('item', {})
                        name = prod.get('name', 'YOK')
                        offers = prod.get('offers', {})
                        price = offers.get('price', 'YOK')
                        if name and price:
                            products.append({"name": name, "price": price})
                    if products:
                        return products
            # Klasik HTML parse fallback
            product_item_sel = selectors.get('product_item')
            if product_item_sel:
                items = soup.select(product_item_sel)
                for el in items:
                    name = el.get_text(strip=True)
                    price = None
                    price_tag = el.find('div', class_='moria-ProductCard-module_price__')
                    if price_tag:
                        price = price_tag.get_text(strip=True)
                    if name:
                        products.append({"name": name, "price": price or "YOK"})
                if products:
                    return products
        except Exception as e:
            print(f"[hepsiburada_plugin][selenium] Hata: {e}")

    return products
