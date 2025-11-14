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

metadata = {
	"name": "example_simple_plugin",
	"version": "0.1.0",
	"description": "Minimal example plugin using requests + BeautifulSoup",
	"supported_sites": ["example.com"],
	"requirements": ["requests", "beautifulsoup4"],
	# Varsayılan selector'lar (config JSON üzerine yazabilir)
	"default_selectors": {
		"product_item": ".product",
		"product_name": ".title",
		"product_price": ".price"
	}
}


def _load_selectors_from_json() -> dict:
	"""Aynı dizindeki .json dosyasından seçicileri yükle.
	
	Plugin plugin_name.py ise, plugin_name.json'dan selector'lar okunur.
	"""
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
	
	# Fallback: metadata'dan varsayılan seçicileri kullan
	return metadata.get("default_selectors", {})


def run(url: str, config: dict) -> list:
	"""Scrape products from `url` and return a list of product dicts.

	Selector'lar şu sırayla yüklenir:
	  1. config['selectors'] (Streamlit'ten geçilirse)
	  2. plugin_name.json dosyası
	  3. metadata['default_selectors']

	Args:
		url: target URL to scrape
		config: configuration dict (can include 'selectors', 'headers', etc.)

	Returns:
		list of dicts: [{"name": str, "price": str, ...}, ...]
	"""
	results = []
	try:
		import requests
		from bs4 import BeautifulSoup

		# Selector'ları yükle (öncelik sırası)
		selectors = config.get("selectors") or _load_selectors_from_json()
		
		headers = config.get("headers") or {"User-Agent": "ecom-scraper/1.0"}
		resp = requests.get(url, headers=headers, timeout=15)
		resp.raise_for_status()
		soup = BeautifulSoup(resp.text, "lxml")

		# --- BEGIN: site-specific extraction (selectors kullan) ---
		product_container = selectors.get("product_container", ".product")
		product_item = selectors.get("product_item", ".product-item")
		product_name = selectors.get("product_name", ".title")
		product_price = selectors.get("product_price", ".price")
		
		print(f"[Plugin] Selector'lar: item={product_item}, name={product_name}, price={product_price}")
		
		product_nodes = soup.select(product_item)
		print(f"[Plugin] Bulunan ürün kartı: {len(product_nodes)}")
		
		for idx, node in enumerate(product_nodes[:20]):
			title_el = node.select_one(product_name)
			price_el = node.select_one(product_price)
			link_el = node.select_one("a")

			title = title_el.get_text(strip=True) if title_el else None
			price = price_el.get_text(strip=True) if price_el else None
			link = link_el.get("href") if link_el else url
			
			print(f"[Plugin] {idx+1}. ürün: {title} | {price}")

			if title and price:
				results.append({"name": title, "price": price, "url": link})
		# --- END: site-specific extraction ---
		
		print(f"[Plugin] Toplam ürün: {len(results)}")

	except Exception as e:
		print(f"[Plugin HATA] {str(e)}")
		raise

	return results


if __name__ == "__main__":
	# Lokal test. Seçicileri _template.json dosyasından yükler
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
