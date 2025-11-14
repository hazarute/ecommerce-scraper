"""
Trendyol ürün kazıyıcı plugin

Sayfa kaynağındaki application/ld+json scriptlerinden ürün verisi çeker, gerekirse CSS selector fallback.
"""
import json
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

metadata = {
    "name": "trendyol_plugin",
    "version": "1.0.0",
    "description": "Trendyol ürün kazıyıcı — JSON-LD öncelikli, CSS fallback.",
    "supported_sites": ["trendyol.com"],
    "requirements": ["requests", "beautifulsoup4", "lxml"],
    "default_selectors": {
        "product_item": "div.p-card-wrppr",
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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        html = resp.text
    except Exception as e:
        print(f"[trendyol_plugin] HTTP Hatası: {e}")
        html = None
    products = []
    # Önce JSON-LD'den ürünleri çekmeye çalış
    found = False
    if html:
        soup = BeautifulSoup(html, "lxml")
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
                found = True
                break
        if found:
            return products
        # JSON-LD bulunamazsa CSS selector fallback
        item_sel = selectors.get('product_item')
        name_sel = selectors.get('product_name')
        price_sel = selectors.get('product_price')
        if not (item_sel and name_sel and price_sel):
            return []
        product_elements = soup.select(item_sel)
        for element in product_elements:
            name_element = element.select_one(name_sel)
            price_element = element.select_one(price_sel)
            name = name_element.get_text(strip=True) if name_element else 'YOK'
            price = price_element.get_text(strip=True) if price_element else 'YOK'
            if name_element and price_element:
                products.append({"name": name, "price": price})
        if products:
            return products
    # Eğer requests ile ürün bulunamazsa Selenium ile dene
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument(f"--user-agent={headers['User-Agent']}")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        page_source = driver.page_source
        driver.quit()
        soup = BeautifulSoup(page_source, "lxml")
        # JSON-LD'den ürünleri çekmeye çalış
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
                found = True
                break
        if found:
            return products
        # JSON-LD bulunamazsa CSS selector fallback
        item_sel = selectors.get('product_item')
        name_sel = selectors.get('product_name')
        price_sel = selectors.get('product_price')
        if not (item_sel and name_sel and price_sel):
            return []
        product_elements = soup.select(item_sel)
        for element in product_elements:
            name_element = element.select_one(name_sel)
            price_element = element.select_one(price_sel)
            name = name_element.get_text(strip=True) if name_element else 'YOK'
            price = price_element.get_text(strip=True) if price_element else 'YOK'
            if name_element and price_element:
                products.append({"name": name, "price": price})
    except Exception as e:
        print(f"[trendyol_plugin][Selenium] Hata: {e}")
    return products
