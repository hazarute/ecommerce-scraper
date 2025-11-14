"""
Smoke Test — app.py Bileşenleri ve İçe Aktarmaları Doğrula

Bu test, app.py'nin temel yapısını ve gerekli importları kontrol eder.
Streamlit UI'da herhangi bir hata olup olmadığını belirler.
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def test_imports():
    """Test 1: Tüm gerekli kütüphanelerin import edilebilir olduğunu kontrol et"""
    print("\n🔍 TEST 1: Kütüphane İçe Aktarımları")
    print("-" * 50)
    
    try:
        import streamlit as st
        print("✅ streamlit")
    except ImportError as e:
        print(f"❌ streamlit: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ pandas")
    except ImportError as e:
        print(f"❌ pandas: {e}")
        return False
    
    try:
        import time
        print("✅ time (stdlib)")
    except ImportError as e:
        print(f"❌ time: {e}")
        return False
    
    try:
        from pathlib import Path
        print("✅ pathlib (stdlib)")
    except ImportError as e:
        print(f"❌ pathlib: {e}")
        return False
    
    try:
        import json
        print("✅ json (stdlib)")
    except ImportError as e:
        print(f"❌ json: {e}")
        return False
    
    print("✅ Tüm kütüphaneler başarıyla import edildi!")
    return True


def test_core_modules():
    """Test 2: Core modüllerin import edilebilir olduğunu kontrol et"""
    print("\n🔍 TEST 2: Core Modülü İçe Aktarımları")
    print("-" * 50)
    
    try:
        from core import engine
        print("✅ core.engine")
        
        # Check for discover_plugins function
        assert hasattr(engine, 'discover_plugins'), "engine.discover_plugins() bulunamadı"
        print("   └─ ✅ discover_plugins() fonksiyonu mevcut")
        
        # Check for run_job function
        assert hasattr(engine, 'run_job'), "engine.run_job() bulunamadı"
        print("   └─ ✅ run_job() fonksiyonu mevcut")
        
    except Exception as e:
        print(f"❌ core.engine: {e}")
        return False
    
    try:
        from utils import exporters
        print("✅ utils.exporters")
        
        # Check for export functions
        assert hasattr(exporters, 'export_csv'), "exporters.export_csv() bulunamadı"
        print("   └─ ✅ export_csv() fonksiyonu mevcut")
        
        assert hasattr(exporters, 'export_json'), "exporters.export_json() bulunamadı"
        print("   └─ ✅ export_json() fonksiyonu mevcut")
        
    except Exception as e:
        print(f"❌ utils.exporters: {e}")
        return False
    
    print("✅ Tüm core modülleri başarıyla import edildi!")
    return True


def test_config_files():
    """Test 3: Konfigürasyon dosyalarının mevcut olduğunu kontrol et"""
    print("\n🔍 TEST 3: Konfigürasyon Dosyaları")
    print("-" * 50)
    
    config_path = project_root / "config" / "sites_config.json"
    
    if config_path.exists():
        print(f"✅ sites_config.json bulundu: {config_path}")
        
        try:
            import json
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print(f"   └─ ✅ JSON parse başarılı ({len(config)} site konfigürasyonu)")
        except Exception as e:
            print(f"   └─ ⚠️  JSON parse hatası: {e}")
    else:
        print(f"⚠️  sites_config.json bulunamadı: {config_path}")
    
    return True


def test_directories():
    """Test 4: Gerekli dizinlerin mevcut olduğunu kontrol et"""
    print("\n🔍 TEST 4: Gerekli Dizinler")
    print("-" * 50)
    
    required_dirs = [
        "core",
        "core/scrapers",
        "utils",
        "custom_plugins",
        "config",
        "data",
        "data/exports",
        "data/logs",
        "data/page_sources",
    ]
    
    all_exist = True
    for dir_name in required_dirs:
        dir_path = project_root / dir_name
        if dir_path.exists():
            print(f"✅ {dir_name}/")
        else:
            print(f"❌ {dir_name}/ (EKSIK)")
            all_exist = False
    
    if all_exist:
        print("✅ Tüm gerekli dizinler mevcut!")
    
    return all_exist


def test_app_py_syntax():
    """Test 5: app.py dosyasının syntax hatası olmadığını kontrol et"""
    print("\n🔍 TEST 5: app.py Syntax Kontrolü")
    print("-" * 50)
    
    app_path = project_root / "app.py"
    
    if not app_path.exists():
        print(f"❌ app.py bulunamadı: {app_path}")
        return False
    
    try:
        with open(app_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        compile(code, str(app_path), 'exec')
        print(f"✅ app.py syntax hatası yok")
        print(f"   └─ {len(code)} karakter, {len(code.splitlines())} satır")
        
    except SyntaxError as e:
        print(f"❌ app.py syntax hatası: {e}")
        return False
    
    return True


def test_plugin_discovery():
    """Test 6: Plugin discovery mekanizmasının çalıştığını kontrol et"""
    print("\n🔍 TEST 6: Plugin Discovery Mekanizması")
    print("-" * 50)
    
    try:
        from core import engine
        plugins = engine.discover_plugins()
        
        print(f"✅ Plugin discovery başarılı")
        print(f"   └─ {len(plugins)} plugin bulundu")
        
        if plugins:
            for p in plugins:
                module = p.get('module', '?')
                meta = p.get('metadata', {})
                name = meta.get('name', module)
                print(f"      • {name} ({module})")
        
        return True
        
    except Exception as e:
        print(f"❌ Plugin discovery hatası: {e}")
        return False


def run_all_tests():
    """Tüm testleri çalıştır ve sonuçları göster"""
    print("\n" + "="*60)
    print("🧪 SMOKE TEST BAŞLATILDI — app.py Bileşen Doğrulaması")
    print("="*60)
    
    results = []
    
    # Run all tests
    results.append(("Kütüphane İçe Aktarımları", test_imports()))
    results.append(("Core Modülleri", test_core_modules()))
    results.append(("Konfigürasyon Dosyaları", test_config_files()))
    results.append(("Gerekli Dizinler", test_directories()))
    results.append(("app.py Syntax", test_app_py_syntax()))
    results.append(("Plugin Discovery", test_plugin_discovery()))
    
    # Summary
    print("\n" + "="*60)
    print("📊 TEST ÖZETI")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status:10} | {test_name}")
    
    print("="*60)
    print(f"Sonuç: {passed}/{total} test geçti")
    
    if passed == total:
        print("🎉 TÜM TESTLER BAŞARILI! app.py hazır.")
        return True
    else:
        print(f"⚠️  {total - passed} test(ler) başarısız. Lütfen kontrol edin.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
