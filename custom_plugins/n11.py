"""
N11 ürün kazıyıcı plugin

Standart HTML selector ile ürün verisi çeker.
"""
import json
import requests
from bs4 import BeautifulSoup
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

metadata = {
    "name": "n11_plugin",
    "version": "1.0.0",
    "description": "N11 ürün kazıyıcı — Standart CSS selector.",
    "supported_sites": ["n11.com"],
    "requirements": ["requests", "beautifulsoup4", "lxml"],
    "default_selectors": {
        "product_item": "li.column",
        "product_name": "h3.productName",
        "product_price": "div.proDetail span.newPrice ins"
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
        print(f"[n11_plugin] HTTP Hatası: {e}")
        html = None
    products = []
    item_sel = selectors.get('product_item')
    name_sel = selectors.get('product_name')
    price_sel = selectors.get('product_price')
    if html:
        soup = BeautifulSoup(html, "lxml")
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
        product_elements = soup.select(item_sel)
        for element in product_elements:
            name_element = element.select_one(name_sel)
            price_element = element.select_one(price_sel)
            name = name_element.get_text(strip=True) if name_element else 'YOK'
            price = price_element.get_text(strip=True) if price_element else 'YOK'
            if name_element and price_element:
                products.append({"name": name, "price": price})
    except Exception as e:
        print(f"[n11_plugin][Selenium] Hata: {e}")
    return products
