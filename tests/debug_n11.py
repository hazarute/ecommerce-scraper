"""
N11 Kazıma Testi — Selector Doğrulaması

Terminal'den çalıştır:
  python tests/debug_n11.py
"""

import requests
from bs4 import BeautifulSoup
from pathlib import Path
import json

# N11 Config
N11_URL = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
N11_SELECTORS = {
    "product_item": "li.column",
    "product_name": "h3.productName",
    "product_price": "div.proDetail span.newPrice ins"
}

def debug_n11():
    print("=" * 70)
    print("🔍 N11 Sitesi — Selector Debug Testi")
    print("=" * 70)
    print(f"\nURL: {N11_URL}\n")
    
    # Headers (N11 bot engelleme var, user-agent şart)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        print("[1] URL'ye bağlanılıyor...")
        resp = requests.get(N11_URL, headers=headers, timeout=15)
        resp.raise_for_status()
        print(f"✅ Status: {resp.status_code}\n")
        
        # HTML kaydet (debug için)
        save_path = Path("tests/n11_debug.html")
        save_path.parent.mkdir(exist_ok=True)
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(resp.text)
        print(f"📄 HTML kaydedildi: {save_path}\n")
        
        # Parse
        soup = BeautifulSoup(resp.text, "lxml")
        
        # Test 1: Product item selector
        print(f"[2] Selector test: '{N11_SELECTORS['product_item']}'")
        items = soup.select(N11_SELECTORS['product_item'])
        print(f"    ✅ Bulunan: {len(items)} ürün kartı\n")
        
        if len(items) == 0:
            print("⚠️  HATA: Ürün kartı bulunamadı!")
            print("    Alternatif selector'lar deniyorum...\n")
            
            # Deneme 1
            alt1 = soup.select("li.prdct")
            print(f"    • 'li.prdct': {len(alt1)} sonuç")
            
            # Deneme 2
            alt2 = soup.select("div.productItem")
            print(f"    • 'div.productItem': {len(alt2)} sonuç")
            
            # Deneme 3
            alt3 = soup.select("div.product")
            print(f"    • 'div.product': {len(alt3)} sonuç")
            
            return
        
        # Test 2-3: Name ve Price için ilk 5 ürünü kontrol et
        print(f"[3] İlk 5 ürün — name ve price selector'ları:\n")
        
        for idx, item in enumerate(items[:5], 1):
            name_el = item.select_one(N11_SELECTORS['product_name'])
            price_el = item.select_one(N11_SELECTORS['product_price'])
            
            name = name_el.get_text(strip=True) if name_el else "❌ BULUNAMADI"
            price = price_el.get_text(strip=True) if price_el else "❌ BULUNAMADI"
            
            print(f"    {idx}. Ürün:")
            print(f"       Name:  {name[:50] if name != '❌ BULUNAMADI' else name}")
            print(f"       Price: {price}\n")
        
        # Debug: HTML snippet
        print("\n[4] HTML Snippet Analizi:\n")
        first_item = items[0] if items else None
        if first_item:
            print(first_item.prettify()[:500])
            print("...")
        
        print("\n" + "=" * 70)
        print("✅ TEST TAMAMLANDI")
        print("=" * 70)
        
    except Exception as e:
        print(f"❌ HATA: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    debug_n11()
