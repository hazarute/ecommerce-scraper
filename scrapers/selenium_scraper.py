from .base_scraper import BaseScraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

class SeleniumScraper(BaseScraper):
    """
    Selenium tabanlı ürün scraper.
    """
    def __init__(self, url, selectors, headless=True, wait_time=5):
        super().__init__(url, selectors)
        self.headless = headless
        self.wait_time = wait_time
        self.last_error = None

    def fetch(self):
        options = Options()
        if self.headless:
            options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument(f"user-agent={self.selectors.get('user_agent', 'Mozilla/5.0')}")
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            driver.get(self.url)
            time.sleep(self.wait_time)  # Sayfanın ve JS'nin yüklenmesi için bekle
            html = driver.page_source
            driver.quit()
            return html
        except Exception as e:
            self.last_error = str(e)
            return None

    def parse(self, html_content):
        if not html_content:
            return []
        soup = BeautifulSoup(html_content, "lxml")
        products = []
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
