from .base_scraper import BaseScraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import os
import json


class SeleniumScraper(BaseScraper):
    """
    Selenium tabanlı ürün scraper.
    """

    def __init__(self, url: str, selectors: dict, headless: bool = True, wait_time: int = 5):
        super().__init__(url, selectors)
        self.headless = headless
        self.wait_time = wait_time

    def fetch(self):
        options = Options()
        if self.headless:
            options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument(f"user-agent={self.selectors.get('user_agent', 'Mozilla/5.0')}")
        driver = None
        try:
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            driver.get(self.url)

            # Ürün kartı selectorunu configten al
            item_sel = self.selectors.get('product_item', None)
            if item_sel:
                # Sadece ilk class'ı al (noktasız)
                first_class = item_sel.split('.')[-1]
                try:
                    WebDriverWait(driver, self.wait_time).until(
                        EC.presence_of_element_located((By.CLASS_NAME, first_class))
                    )
                except Exception as e:
                    print(f"[SeleniumScraper UYARI]: WebDriverWait ile ürün kartı beklenirken hata: {e}")
            else:
                time.sleep(self.wait_time)

            html = driver.page_source

            # Debug: Sayfa kaynağını dosyaya kaydet (yeni konum)
            save_dir = os.path.join('data', 'page_sources')
            os.makedirs(save_dir, exist_ok=True)
            save_path = os.path.join(save_dir, 'last_page_source.html')
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(html)

            # Kaydedilen dosya ile dönen html aynı mı?
            try:
                with open(save_path, 'r', encoding='utf-8') as f:
                    saved_html = f.read()
                if html == saved_html:
                    print('[DEBUG] fetch() dönen html ile kaydedilen data/page_sources/last_page_source.html birebir aynı.')
                else:
                    print('[DEBUG] fetch() dönen html ile kaydedilen data/page_sources/last_page_source.html FARKLI!')
            except Exception:
                print('[DEBUG] Kaydedilen sayfa okuma sırasında hata.')

            return html
        except Exception as e:
            self.last_error = str(e)
            print(f"[SeleniumScraper HATA]: {self.last_error}")
            return None
        finally:
            if driver:
                try:
                    driver.quit()
                except Exception:
                    pass

    def parse(self, html_content: str):
        if not html_content:
            print('[DEBUG-parse] html_content boş!')
            return []
        # Generic parse: CSS selector ile ürünleri çek
        soup = BeautifulSoup(html_content, "lxml")
        products = []
        item_sel = self.selectors.get('product_item', None)
        name_sel = self.selectors.get('product_name', None)
        price_sel = self.selectors.get('product_price', None)
        print(f'[DEBUG-parse][generic] Selectorlar: item={item_sel}, name={name_sel}, price={price_sel}')
        if not (item_sel and name_sel and price_sel):
            print('[DEBUG-parse][generic] Selectorlar eksik!')
            return []
        product_elements = soup.select(item_sel)
        print(f'[DEBUG-parse][generic] Bulunan ürün kartı: {len(product_elements)}')
        for idx, element in enumerate(product_elements[:20]):
            name_element = element.select_one(name_sel)
            price_element = element.select_one(price_sel)
            name = name_element.get_text(strip=True) if name_element else 'YOK'
            price = price_element.get_text(strip=True) if price_element else 'YOK'
            print(f'[DEBUG-parse][generic] {idx+1}. ürün: {name} | {price}')
            if name_element and price_element:
                products.append({"name": name, "price": price})
        print(f'[DEBUG-parse][generic] Sonuç ürün sayısı: {len(products)}')
        return products
