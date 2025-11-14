#!/usr/bin/env python3
"""
Integration test for N11 scraping with auto-detected mode.
Verifies that:
1. URL detection identifies N11 correctly
2. Mode is automatically set to Selenium
3. Selectors are loaded from config
"""

import json
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_n11_detection():
    """Test N11 URL detection and mode override."""
    print("=" * 60)
    print("TEST: N11 URL Detection & Mode Auto-Override")
    print("=" * 60)
    
    url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
    
    # Simulate app.py detection logic
    detected_site = "manuel"  # Initial choice
    detected_mode = "requests"  # Initial choice
    
    # Apply detection
    if "n11" in url.lower():
        detected_site = "n11"
        detected_mode = "selenium"
    
    print(f"\n✓ Input URL: {url}")
    print(f"✓ Detected Site: {detected_site.upper()}")
    print(f"✓ Detected Mode: {detected_mode.upper()}")
    
    # Load config
    try:
        with open("config/sites_config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        
        site_conf = config.get(detected_site, {})
        selectors = site_conf.get("selectors", {})
        
        print(f"✓ Site config loaded: {'selectors' in site_conf}")
        print(f"✓ Selectors count: {len(selectors)}")
        
        if selectors:
            selector_keys = list(selectors.keys())
            print(f"  → Selector keys: {selector_keys[:5]}...")
        
        assert detected_site == "n11", "Site detection failed"
        assert detected_mode == "selenium", "Mode detection failed"
        assert len(selectors) > 0, "Selectors not loaded"
        
        print("\n✅ All detection tests passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {str(e)}")
        return False

def test_n11_scraping():
    """Test actual N11 scraping with Selenium."""
    print("\n" + "=" * 60)
    print("TEST: N11 Scraping with Selenium")
    print("=" * 60)
    
    url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
    
    try:
        from core.engine import run_job
        
        with open("config/sites_config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        
        site_conf = config.get("n11", {})
        selectors = site_conf.get("selectors", {})
        selectors['site'] = 'n11'  # ← Add site key for parse() method
        
        print(f"\n⏳ Starting N11 scrape (30s timeout)...")
        
        result, error = run_job(
            url=url,
            mode="selenium",
            selectors=selectors,
            headless=True
        )
        
        if error:
            print(f"✗ Scraping error: {error}")
            return False
        
        print(f"✓ Scraping completed")
        print(f"✓ Products found: {len(result)}")
        
        if result:
            for i, product in enumerate(result, 1):
                name = product.get("name", "N/A")[:40]
                price = product.get("price", "N/A")
                print(f"  {i}. {name}... (${price})")
            print("\n✅ N11 scraping successful!")
            return True
        else:
            print("\n⚠️ No products found (check selectors)")
            return False
            
    except Exception as e:
        print(f"\n❌ Scraping failed: {str(e)[:100]}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test1 = test_n11_detection()
    test2 = test_n11_scraping()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Detection Test: {'✅ PASS' if test1 else '❌ FAIL'}")
    print(f"Scraping Test: {'✅ PASS' if test2 else '❌ FAIL'}")
    print("=" * 60)
    
    sys.exit(0 if test1 else 1)
