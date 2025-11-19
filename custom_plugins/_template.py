"""
Example plugin template for `custom_plugins/`.

Plugin Mimarisi:
  1. Bu dosyayı `custom_plugins/my_site_scraper.py` olarak kopyala
  2. Aynı dizine `my_site_scraper.json` dosyası oluştur (selector'lar burada)
  3. `metadata` ve `run()` fonksiyonunu güncelle
  4. `core/engine.py` otomatik olarak .json config dosyasını yükleyecek

Contract:
  - `metadata` (dict) with plugin information
  - `def run(url: str, config: dict) -> list` returns List[Dict]
  - Selector'lar `config['selectors']` veya `my_site_scraper.json` dosyasından gelir
"""

import json
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import random
import time

# Selenium fallback için
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    webdriver = None

metadata = {
    "name": "example_simple_plugin",
    "version": "0.2.0",
    "description": "Minimal example plugin using requests + BeautifulSoup, with Selenium fallback",
    "supported_sites": ["example.com"],
    "requirements": ["requests", "beautifulsoup4"],
    "default_selectors": {
        "product_item": ".product",
        "product_name": ".title",
        "product_price": ".price"
    }
}

def _load_selectors_from_json() -> dict:
    """Aynı dizindeki .json dosyasından seçicileri yükle."""
    current_file = Path(__file__)
    config_file = current_file.parent / f"{current_file.stem}.json"
    if config_file.exists():
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print(f"[Plugin] Selector'lar {config_file.name} dosyasından yüklendi")
            return config.get("selectors", {})
        except Exception as e:
            print(f"[Plugin UYARI] {config_file.name} okunurken hata: {e}")
    return metadata.get("default_selectors", {})

def run(url: str, config: dict) -> list:
    """Scrape products from `url` and return a list of product dicts."""
    results = []
    print(f"[Plugin] Başlatılıyor: {metadata['name']} v{metadata['version']}")
    print(f"[Plugin] Hedef URL: {url}")
    try:
        # Selector'ları yükle
        selectors = config.get("selectors") or _load_selectors_from_json()
        headers = config.get("headers") or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
        }

        print("[Plugin] Requests ile veri çekme denemesi başlıyor...")
        # Önce requests ile dene
        try:
            resp = requests.get(url, headers=headers, timeout=15)
            resp.raise_for_status()
            html = resp.text
            print("[Plugin] Requests ile veri çekme başarılı.")
        except Exception as e:
            print(f"[Plugin] Requests ile veri çekme başarısız: {e}")
            html = None

        if html:
            print("[Plugin] HTML parse işlemi başlıyor...")
            soup = BeautifulSoup(html, "lxml")
            product_item = selectors.get("product_item", ".product")
            product_name = selectors.get("product_name", ".title")
            product_price = selectors.get("product_price", ".price")

            product_nodes = soup.select(product_item)
            print(f"[Plugin] Bulunan ürün kartı sayısı: {len(product_nodes)}")
            for idx, node in enumerate(product_nodes):
                try:
                    name_el = node.select_one(product_name)
                    name = name_el.get_text(strip=True) if name_el else None

                    price_el = node.select_one(product_price)
                    price = price_el.get_text(strip=True) if price_el else None

                    if name and price:
                        results.append({"name": name, "price": price})
                        print(f"[Plugin] {idx + 1}. Ürün: {name} | {price}")
                except Exception as e:
                    print(f"[Plugin] Ürün işlenirken hata: {e}")
                    continue

        # Eğer requests ile veri bulunamazsa Selenium ile dene
        if not results and webdriver is not None:
            print("[Plugin] Selenium fallback başlatılıyor...")
            try:
                options = Options()
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                options.add_argument('--no-sandbox')
                options.add_argument('--window-size=1920,1080')
                options.add_argument(f'user-agent={headers["User-Agent"]}')

                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
                driver.get(url)
                print("[Plugin][Selenium] Sayfa yüklendi, HTML parse işlemi başlıyor...")
                time.sleep(3)
                html = driver.page_source
                driver.quit()

                soup = BeautifulSoup(html, "lxml")
                product_nodes = soup.select(selectors.get("product_item", ".product"))
                print(f"[Plugin][Selenium] Bulunan ürün kartı sayısı: {len(product_nodes)}")
                for idx, node in enumerate(product_nodes):
                    try:
                        name_el = node.select_one(selectors.get("product_name", ".title"))
                        name = name_el.get_text(strip=True) if name_el else None

                        price_el = node.select_one(selectors.get("product_price", ".price"))
                        price = price_el.get_text(strip=True) if price_el else None

                        if name and price:
                            results.append({"name": name, "price": price})
                            print(f"[Plugin][Selenium] {idx + 1}. Ürün: {name} | {price}")
                    except Exception as e:
                        print(f"[Plugin][Selenium] Ürün işlenirken hata: {e}")
                        continue
            except Exception as e:
                print(f"[Plugin][Selenium] Hata: {e}")

    except Exception as e:
        print(f"[Plugin] Genel Hata: {e}")

    print(f"[Plugin] Toplam bulunan ürün sayısı: {len(results)}")
    return results

if __name__ == "__main__":
    # Lokal test
    test_url = "https://example.com/"
    cfg = {}  # Boş bırakırsan _template.json'dan yükler
    print("Plugin test çalışıyor:", test_url)
    try:
        out = run(test_url, cfg)
        print(f"Bulunan {len(out)} ürün:")
        for i, p in enumerate(out[:5], 1):
            print(f"  {i}. {p}")
    except Exception as err:
        print(f"Plugin hatası: {err}")
