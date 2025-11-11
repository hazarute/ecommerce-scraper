# Teknik Detaylar

## 1. Teknolojiler ve Sürümler

- **Programlama Dili:** Python (Sürüm 3.6 veya üzeri)
- **Temel Kütüphaneler:**
    - `requests`: HTTP isteklerini basitleştirmek için. Web sitelerinden HTML içeriğini almak için kullanılır.
    - `beautifulsoup4`: HTML ve XML dosyalarını ayrıştırmak için. HTML içeriğinden belirli veri parçalarını (ürün adı, fiyat vb.) çıkarmak için kullanılır.
- **Yardımcı Kütüphaneler:**
    - `lxml`: `BeautifulSoup` için yüksek performanslı bir HTML ayrıştırıcısı olarak önerilir, ancak başlangıç için zorunlu değildir. `requirements.txt` dosyasına dahil edilecektir.

## 2. Geliştirme Ortamı Kurulumu

1.  **Python Kurulumu:**
    - Sistemde Python 3.6 veya daha yeni bir sürümün kurulu olduğundan emin olun.
    - Kurulumu doğrulamak için terminalde `python --version` komutunu çalıştırın.

2.  **Proje Klonlama:**
    - Proje dosyalarını yerel makinenize indirmek için Git kullanın:
      ```bash
      git clone https://github.com/hazarute/ecommerce-scraper.git
      cd ecommerce-scraper
      ```

3.  **Sanal Ortam (Önerilir):**
    - Proje bağımlılıklarını sistem genelindeki paketlerden izole etmek için bir sanal ortam oluşturulması şiddetle tavsiye edilir.
      ```bash
      python -m venv venv
      ```
    - Sanal ortamı etkinleştirin:
      - Windows: `.\venv\Scripts\activate`
      - macOS/Linux: `source venv/bin/activate`

4.  **Bağımlılıkların Yüklenmesi:**
    - Gerekli tüm Python kütüphanelerini yüklemek için `pip` kullanın:
      ```bash
      pip install -r requirements.txt
      ```

## 3. Bağımlılık Yönetimi

- Projenin tüm Python bağımlılıkları, kök dizinde bulunan `requirements.txt` dosyasında listelenir.
- Yeni bir bağımlılık eklendiğinde, bu dosyaya eklenmelidir.
- `requirements.txt` içeriği:
  ```
  requests
  beautifulsoup4
  lxml
  ```

## 4. Projeyi Çalıştırma

- Kurulum tamamlandıktan ve (varsa) sanal ortam etkinleştirildikten sonra, kazıyıcıyı çalıştırmak için aşağıdaki komutu kullanın:
  ```bash
  python scraper.py
  ```

## 5. Teknik Kısıtlamalar ve Bilinen Sınırlar

- **JavaScript Oluşturulan İçerik:** Bu kazıyıcı, yalnızca sunucudan gelen ilk HTML yanıtını işleyebilir. Eğer bir web sitesi ürün bilgilerini JavaScript kullanarak sonradan yüklüyorsa (dinamik içerik), bu araç o verileri göremez. Bu tür siteler için Selenium veya Scrapy gibi daha gelişmiş araçlar gerekir.
- **Kazıma Engelleri:** Birçok modern e-ticaret sitesi, otomatik kazıma girişimlerini engellemek için Cloudflare gibi güvenlik önlemleri veya CAPTCHA'lar kullanır. Bu kazıyıcı, bu tür engelleri aşmak için herhangi bir mekanizma içermez.
- **Hız Sınırlamaları (Rate Limiting):** Sunucuyu aşırı yüklememek ve IP adresinin engellenmesini önlemek için istekler arasında gecikme eklenmemiştir. Yüksek frekanslı kullanım için bu bir risk faktörüdür.
