# Custom Plugins  Geliştirici Kılavuzu

Müşterinin özel kazıyıcılarını custom_plugins/ klasörüne ekleyin.

##  Yeni Plugin Ekleme

### Dosya Yapısı
`
custom_plugins/
 _template.py              # Template
 my_site_scraper.py        # Plugin kodu
 my_site_scraper.json      # Seçiciler (ÖNERİLEN)
`

### Adımlar
1. _template.py kopyala  my_site_scraper.py
2. example_amazon.json kopyala  my_site_scraper.json
3. Seçicileri .json dosyasında güncelle
4. Plugin kodunu düzenle
5. Test: python custom_plugins/my_site_scraper.py
6. Streamlit'te kullan:  "plugin"  "custom_plugins.my_site_scraper"

##  Seçici Yükleme Sırası

1. Streamlit'ten config['selectors']
2. Plugin .json dosyası
3. metadata['default_selectors']

##  Örnek
Bkz: example_amazon.py + example_amazon.json

##  Güvenlik
- Production: plugin metadata valide et
- Plugins sandbox/container'da çalıştır
- Kod review yap

