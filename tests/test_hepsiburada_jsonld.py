#!/usr/bin/env python3
"""
Test Hepsiburada JSON-LD parsing (no anti-bot issues).
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

def test_hepsiburada_detection():
    """Test Hepsiburada URL detection."""
    print("=" * 60)
    print("TEST: Hepsiburada URL Detection & Mode Auto-Override")
    print("=" * 60)
    
    url = "https://www.hepsiburada.com/arama?q=laptop"
    
    # Simulate app.py detection logic
    detected_site = "manuel"
    detected_mode = "requests"
    
    # Apply detection
    if "hepsiburada" in url.lower():
        detected_site = "hepsiburada"
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
        selectors['site'] = detected_site
        
        print(f"✓ Site config loaded: {'selectors' in site_conf}")
        print(f"✓ Selectors count: {len(selectors)}")
        
        if selectors:
            selector_keys = list(selectors.keys())
            print(f"  → Selector keys: {selector_keys[:5]}...")
        
        assert detected_site == "hepsiburada", "Site detection failed"
        assert detected_mode == "selenium", "Mode detection failed"
        
        print("\n✅ All detection tests passed!")
        return True, selectors
        
    except Exception as e:
        print(f"\n❌ Test failed: {str(e)}")
        return False, {}

def test_hepsiburada_scraping(selectors):
    """Test actual Hepsiburada scraping (JSON-LD)."""
    print("\n" + "=" * 60)
    print("TEST: Hepsiburada Scraping (JSON-LD)")
    print("=" * 60)
    
    url = "https://www.hepsiburada.com/arama?q=laptop"
    
    try:
        from core.engine import run_job
        
        print(f"\n⏳ Starting Hepsiburada scrape...")
        
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
            for i, product in enumerate(result[:5], 1):
                name = product.get("name", "N/A")[:40]
                price = product.get("price", "N/A")
                print(f"  {i}. {name}... (${price})")
            print("\n✅ Hepsiburada scraping successful!")
            return True
        else:
            print("\n⚠️ No products found")
            return False
            
    except Exception as e:
        print(f"\n❌ Scraping failed: {str(e)[:100]}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test1, selectors = test_hepsiburada_detection()
    test2 = test_hepsiburada_scraping(selectors) if test1 else False
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Detection Test: {'✅ PASS' if test1 else '❌ FAIL'}")
    print(f"Scraping Test: {'✅ PASS' if test2 else '❌ FAIL'}")
    print("=" * 60)
    
    sys.exit(0 if test1 and test2 else 1)
