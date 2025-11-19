import os
import time
from datetime import datetime
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def fetch_page_source():
    # Kullanıcıdan hedef URL'yi al
    target_url = input("🔗 Hedef URL'yi girin: ").strip()
    if not target_url:
        print("❌ Hata: Geçerli bir URL girilmedi.")
        return

    # URL'den domain adını çıkar
    parsed_url = urlparse(target_url)
    domain = parsed_url.netloc.replace("www.", "").split(".")[0]

    # Dosya adı için timestamp oluştur
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{domain}_{timestamp}.html"

    # Kaydetme klasörünü ayarla
    save_dir = os.path.join("data", "page_sources")
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, filename)

    # Selenium seçeneklerini ayarla
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    )

    # WebDriver başlat
    driver = None
    try:
        print("🌐 Sayfa yükleniyor...")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(target_url)

        # Sayfanın tam yüklenmesi için bekle
        time.sleep(5)

        # Sayfa kaynağını al ve kaydet
        page_source = driver.page_source
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(page_source)

        print(f"✅ Kaynak kod kaydedildi: {save_path}")
    except Exception as e:
        print(f"❌ Hata: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    fetch_page_source()