"""
Akakçe ürün kazıyıcı plugin

Sayfa kaynağındaki ürünleri çekmek için requests ve BeautifulSoup kullanır.
"""

import json
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import random
import time

metadata = {
    "name": "akakce_plugin",
    "version": "1.0.1",
    "description": "Akakçe ürün kazıyıcı — Standart CSS selector.",
    "supported_sites": ["akakce.com"],
    "example_url": "https://www.akakce.com/filtre-kahve-makinesi.html"
}


def _load_selectors_from_json() -> dict:
    """Aynı dizindeki .json dosyasından seçicileri yükle."""
    current_file = Path(__file__)
    config_file = current_file.parent / f"{current_file.stem}.json"
    if config_file.exists():
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print(f"[Akakçe Plugin] Selector'lar {config_file.name} dosyasından yüklendi")
            return config.get("selectors", {})
        except Exception as e:
            print(f"[Akakçe Plugin UYARI] {config_file.name} okunurken hata: {e}")
    return {}


# Selenium fallback için
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    webdriver = None


def run(url: str, config: dict) -> list:
    """Akakçe'den ürünleri kazı."""
    results = []
    try:
        # Selector'ları yükle
        selectors = config.get("selectors") or _load_selectors_from_json()
        headers = config.get("headers") or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Referer": "https://www.google.com/",
            "DNT": "1",
            "Connection": "keep-alive"
        }

        # Önce requests ile dene
        try:
            resp = requests.get(url, headers=headers, timeout=15)
            resp.raise_for_status()
            html = resp.text
        except Exception as e:
            print(f"[Akakçe Plugin] HTTP Hatası: {e}")
            html = None

        if html:
            soup = BeautifulSoup(html, "lxml")
            # Ürünleri işle (requests ile)
            product_container = selectors.get("product_container", "ul#CPL > li")
            product_name = selectors.get("product_name", "h3.pn_v8")
            product_price = selectors.get("product_price", "span.pt_v9")
            product_link = selectors.get("product_link", "a")

            product_nodes = soup.select(product_container)
            for idx, node in enumerate(product_nodes):
                try:
                    name_el = node.select_one(product_name)
                    name = name_el.get_text(strip=True) if name_el else None

                    price_el = node.select_one(product_price)
                    price = price_el.get_text(strip=True) if price_el else None
                    if price:
                        price = price.replace("TL", "").replace("kr", "").replace(",", ".").strip()

                    link_el = node.select_one(product_link)
                    link = link_el.get("href") if link_el else None
                    if link and not link.startswith("http"):
                        link = f"https://www.akakce.com{link}"

                    if name and price:
                        results.append({"name": name, "price": price, "url": link})
                except Exception as e:
                    print(f"[Akakçe Plugin] Ürün işlenirken hata: {e}")
                    continue

        # Eğer requests ile veri bulunamazsa Selenium ile dene
        if not results and webdriver is not None:
            try:
                options = Options()
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                options.add_argument('--no-sandbox')
                options.add_argument('--window-size=1920,1080')
                options.add_argument(f'user-agent={headers["User-Agent"]}')

                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
                driver.get(url)
                time.sleep(3)
                html = driver.page_source
                driver.quit()

                soup = BeautifulSoup(html, "lxml")
                product_nodes = soup.select(selectors.get("product_container", "ul#CPL > li"))
                for idx, node in enumerate(product_nodes):
                    try:
                        name_el = node.select_one(selectors.get("product_name", "h3.pn_v8"))
                        name = name_el.get_text(strip=True) if name_el else None

                        price_el = node.select_one(selectors.get("product_price", "span.pt_v9"))
                        price = price_el.get_text(strip=True) if price_el else None
                        if price:
                            price = price.replace("TL", "").replace("kr", "").replace(",", ".").strip()

                        link_el = node.select_one(selectors.get("product_link", "a"))
                        link = link_el.get("href") if link_el else None
                        if link and not link.startswith("http"):
                            link = f"https://www.akakce.com{link}"

                        if name and price:
                            results.append({"name": name, "price": price, "url": link})
                    except Exception as e:
                        print(f"[Akakçe Plugin][Selenium] Ürün işlenirken hata: {e}")
                        continue
            except Exception as e:
                print(f"[Akakçe Plugin][Selenium] Hata: {e}")

    except Exception as e:
        print(f"[Akakçe Plugin] Genel Hata: {e}")

    return results


if __name__ == "__main__":
    # Lokal test
    test_url = "https://www.akakce.com/filtre-kahve-makinesi.html"
    cfg = {}  # Boş bırakırsan akakce.json'dan yükler
    print("Plugin test çalışıyor:", test_url)
    try:
        out = run(test_url, cfg)
        print(f"Bulunan {len(out)} ürün:")
        for i, p in enumerate(out[:5], 1):
            print(f"  {i}. {p}")
    except Exception as err:
        print(f"Plugin hatası: {err}")