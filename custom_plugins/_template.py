"""
Example plugin template for `custom_plugins/`.

Contract:
  - `metadata` (dict) with plugin information
  - `def run(url: str, config: dict) -> list` returns List[Dict]

This file is intentionally simple — copy it to `custom_plugins/my_plugin.py`,
update `metadata` and implement `run()` for your site.
"""

metadata = {
	"name": "example_simple_plugin",
	"version": "0.1.0",
	"description": "Minimal example plugin using requests + BeautifulSoup",
	"supported_sites": ["example.com"],
	# optional: list of PyPI package names required by this plugin
	"requirements": ["requests", "beautifulsoup4"],
}


def run(url: str, config: dict) -> list:
	"""Scrape products from `url` and return a list of product dicts.

	Note: This example uses naive selectors and is intended as a template.

	Args:
		url: target URL to scrape
		config: configuration dict (from Streamlit UI or caller)

	Returns:
		list of dicts: [{"title": str, "price": str, "url": str, ...}, ...]
	"""
	results = []
	try:
		import requests
		from bs4 import BeautifulSoup

		headers = config.get("headers") or {"User-Agent": "ecom-scraper/0.1"}
		resp = requests.get(url, headers=headers, timeout=15)
		resp.raise_for_status()
		soup = BeautifulSoup(resp.text, "lxml")

		# --- BEGIN: site-specific extraction (replace with real selectors) ---
		# This is intentionally generic. Update the selectors below.
		product_nodes = soup.select(config.get("product_container", ".product"))
		for node in product_nodes[:20]:
			title_el = node.select_one(config.get("product_name", ".title"))
			price_el = node.select_one(config.get("product_price", ".price"))
			link_el = node.select_one("a")

			title = title_el.get_text(strip=True) if title_el else None
			price = price_el.get_text(strip=True) if price_el else None
			link = link_el.get("href") if link_el else url

			results.append({"title": title, "price": price, "url": link})
		# --- END: site-specific extraction ---

	except Exception as e:
		# Follow engine convention: return an error object or empty list
		# Here we re-raise so the engine can capture/log it. Alternatively,
		# return [{"error": True, "message": str(e)}]
		raise

	return results


if __name__ == "__main__":
	# Simple local test runner. Update `test_url` and `cfg` for your site.
	test_url = "https://example.com/"
	cfg = {
		"product_container": ".product",
		"product_name": ".title",
		"product_price": ".price",
	}
	print("Running example plugin against:", test_url)
	try:
		out = run(test_url, cfg)
		print("Found", len(out), "items")
		for i, p in enumerate(out[:5], 1):
			print(i, p)
	except Exception as err:
		print("Plugin test failed:", err)
