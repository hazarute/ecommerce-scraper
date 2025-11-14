"""
Generic Requests tabanlı ürün kazıyıcı
Verilen URL ve selector dict ile ürünleri çeker.
"""
import requests
from bs4 import BeautifulSoup

def run(url: str, selectors: dict, user_agent: str = None, timeout: int = 30) -> list:
    headers = {"User-Agent": user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    try:
        resp = requests.get(url, headers=headers, timeout=timeout)
        resp.raise_for_status()
        html = resp.text
    except Exception as e:
        print(f"[generic_requests_scraper] HTTP Hatası: {e}")
        return []
    products = []
    found = False
    # Önce JSON-LD'den ürünleri çekmeye çalış
    soup = BeautifulSoup(html, "lxml")
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
