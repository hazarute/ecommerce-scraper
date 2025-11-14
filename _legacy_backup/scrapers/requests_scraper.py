from .base_scraper import BaseScraper
import requests
from bs4 import BeautifulSoup

class RequestsScraper(BaseScraper):
    """
    Requests tabanlı ürün scraper.
    """
    def fetch(self):
        try:
            response = requests.get(self.url, headers=self.selectors.get('headers', {}), timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            self.last_error = str(e)
            return None

    def parse(self, html_content):
        if not html_content:
            return []
        soup = BeautifulSoup(html_content, "lxml")
        products = []
        # Seçiciler config dosyasından gelmeli
        container_sel = self.selectors.get('product_container', None)
        item_sel = self.selectors.get('product_item', None)
        name_sel = self.selectors.get('product_name', None)
        price_sel = self.selectors.get('product_price', None)
        if not (container_sel and item_sel and name_sel and price_sel):
            return []
        container = soup.select_one(container_sel) if container_sel else soup
        product_elements = container.select(item_sel) if container else []
        for element in product_elements[:5]:
            name_element = element.select_one(name_sel)
            price_element = element.select_one(price_sel)
            if name_element and price_element:
                name = name_element.get_text(strip=True)
                price = price_element.get_text(strip=True)
                products.append({"name": name, "price": price})
        return products
