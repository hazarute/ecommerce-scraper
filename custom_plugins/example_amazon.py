"""
Amazon ürün kazıyıcı plugin — Başlangıç Örneği

Bu plugin örneği, Selenium veya Requests kullanarak Amazon'dan ürün kazır.
Selector'lar `example_amazon.json` dosyasından yüklenir.

Kullanım:
  1. custom_plugins/example_amazon.py (bu dosya)
  2. custom_plugins/example_amazon.json (seçiciler)
  3. Streamlit UI'da "Plugin" modunu seç → "custom_plugins.example_amazon" seç
  4. URL: https://www.amazon.com/s?k=laptop
"""

import json
from pathlib import Path

metadata = {
	"name": "amazon_scraper",
	"version": "1.0.0",
	"description": "Amazon ürün kazıyıcı — Requests + BeautifulSoup",
	"supported_sites": ["amazon.com", "amazon.co.uk"],
	"requirements": ["requests", "beautifulsoup4", "lxml"],
	"default_selectors": {
		"product_item": "div.s-result-item",
		"product_name": "h2 span",
		"product_price": "span.a-price-whole"
	}
}


def _load_selectors_from_json() -> dict:
	"""Aynı dizindeki .json dosyasından seçicileri yükle.
	
	example_amazon.py ise, example_amazon.json'dan selector'lar okunur.
	"""
	current_file = Path(__file__)
	config_file = current_file.parent / f"{current_file.stem}.json"
	
	if config_file.exists():
		try:
			with open(config_file, 'r', encoding='utf-8') as f:
				config = json.load(f)
			print(f"[Amazon Plugin] Selector'lar {config_file.name} dosyasından yüklendi")
			return config.get("selectors", {})
		except Exception as e:
			print(f"[Amazon Plugin UYARI] {config_file.name} okunurken hata: {e}")
	
	# Fallback: metadata'dan varsayılan seçicileri kullan
	return metadata.get("default_selectors", {})


def run(url: str, config: dict) -> list:
	"""Amazon'dan ürün kazı.

	Selector'lar şu sırayla yüklenir:
	  1. config['selectors'] (Streamlit'ten geçilirse)
	  2. example_amazon.json dosyası
	  3. metadata['default_selectors']

	Args:
		url: target URL to scrape (e.g., https://www.amazon.com/s?k=laptop)
		config: configuration dict (can include 'selectors', 'headers', etc.)

	Returns:
		list of dicts: [{"name": str, "price": str, "url": str, ...}, ...]
	"""
	results = []
	try:
		import requests
		from bs4 import BeautifulSoup

		# Selector'ları yükle (öncelik sırası)
		selectors = config.get("selectors") or _load_selectors_from_json()
		
		# Headers hazırla
		headers = config.get("headers") or {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
		}
		
		print(f"[Amazon Plugin] URL'ye bağlanılıyor: {url}")
		resp = requests.get(url, headers=headers, timeout=15)
		resp.raise_for_status()
		soup = BeautifulSoup(resp.text, "lxml")

		# Amazon özgü seçiciler
		product_item = selectors.get("product_item", "div.s-result-item")
		product_name = selectors.get("product_name", "h2 span")
		product_price = selectors.get("product_price", "span.a-price-whole")
		product_image = selectors.get("product_image", "img.s-image")
		
		print(f"[Amazon Plugin] Selector'lar: item={product_item}, name={product_name}, price={product_price}")
		
		# Ürünleri kazı
		product_nodes = soup.select(product_item)
		print(f"[Amazon Plugin] Bulunan ürün kartı: {len(product_nodes)}")
		
		for idx, node in enumerate(product_nodes[:20]):
			try:
				# Ürün başlığı
				title_el = node.select_one(product_name)
				title = title_el.get_text(strip=True) if title_el else None
				
				# Ürün fiyatı
				price_el = node.select_one(product_price)
				price = price_el.get_text(strip=True) if price_el else None
				
				# Ürün linki
				link_el = node.select_one("a")
				link = link_el.get("href") if link_el else url
				if link and not link.startswith("http"):
					link = "https://amazon.com" + link
				
				# Resim URL'si (opsiyonel)
				image_el = node.select_one(product_image)
				image_url = image_el.get("src") if image_el else None
				
				if title and price:
					print(f"[Amazon Plugin] {idx+1}. ürün: {title[:50]}... | {price}")
					results.append({
						"name": title,
						"price": price,
						"url": link,
						"image_url": image_url
					})
			except Exception as item_err:
				print(f"[Amazon Plugin] Ürün {idx+1} işlenirken hata: {item_err}")
				continue
		
		print(f"[Amazon Plugin] Toplam ürün kazıldı: {len(results)}")

	except Exception as e:
		print(f"[Amazon Plugin HATA] {str(e)}")
		raise

	return results


if __name__ == "__main__":
	# Lokal test — komut satırından çalıştır:
	# python custom_plugins/example_amazon.py
	
	test_url = "https://www.amazon.com/s?k=laptop"
	cfg = {}  # Boş bırakırsan example_amazon.json'dan yükler
	
	print("=" * 60)
	print("Amazon Plugin — Lokal Test")
	print("=" * 60)
	print(f"URL: {test_url}\n")
	
	try:
		out = run(test_url, cfg)
		print(f"\n✅ Başarılı! {len(out)} ürün kazıldı:\n")
		for i, p in enumerate(out[:5], 1):
			print(f"{i}. {p['name'][:40]}...")
			print(f"   Fiyat: {p['price']}")
			print(f"   URL: {p['url']}\n")
	except Exception as err:
		print(f"\n❌ Plugin hatası: {err}")
