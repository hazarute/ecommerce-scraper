"""
Generic Selenium tabanlı ürün kazıyıcı
Verilen URL ve selector dict ile ürünleri çeker.
"""
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def run(url: str, selectors: dict, user_agent: str = None, timeout: int = 30, headless: bool = True) -> list:
    import time
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
    if user_agent:
        chrome_options.add_argument(f"--user-agent={user_agent}")
    else:
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(timeout)
    try:
        driver.get(url)
        time.sleep(5)  # Dinamik içerik için bekle
        page_source = driver.page_source
        # Debug: page_source'u kaydet
        try:
            with open("data/page_sources/last_page_source.html", "w", encoding="utf-8") as f:
                f.write(page_source)
        except Exception as e:
            print(f"[generic_selenium_scraper] page_source kaydedilemedi: {e}")
    except Exception as e:
        print(f"[generic_selenium_scraper] Selenium Hatası: {e}")
        driver.quit()
        return []
    driver.quit()
    soup = BeautifulSoup(page_source, "lxml")
    products = []
    found = False
    # Önce JSON-LD'den ürünleri çekmeye çalış
    json_ld_tags = soup.find_all('script', type='application/ld+json')
    for tag in json_ld_tags:
        try:
            data = json.loads(tag.string)
        except Exception:
            continue
        # ItemList veya Product tipinde JSON-LD
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
        # Tekil ürün (Product) desteği
        if isinstance(data, dict) and data.get('@type') == 'Product':
            name = data.get('name', 'YOK')
            offers = data.get('offers', {})
            price = offers.get('price', 'YOK')
            if name and price:
                products.append({"name": name, "price": price})
            found = True
            break
    if found and products:
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
    return products
