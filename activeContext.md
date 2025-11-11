# Aktif Bağlam - Strateji Defteri

## Mevcut Çalışma Odağı
Kullanıcıya Hepsiburada, Trendyol, N11 gibi popüler siteleri varsayılan olarak sunan ve manuel girişe izin veren bir konsol arayüzü ile esnek ve kullanıcı dostu bir deneyim sağlamak.

## Aktif Kararlar ve Gerekçeler

1.  **Kullanıcıdan Dinamik URL ve Site Seçimi:**
    *   **Karar:** Script başlatılırken kullanıcıya Hepsiburada, Trendyol, N11 gibi popüler sitelerden birini seçme veya manuel URL girme seçeneği sunulacak.
    *   **Gerekçe:** Kodun sadece sabit bir siteye bağlı kalmasını önler, farklı sitelerle test etmeyi ve genişletmeyi kolaylaştırır. Eğitimsel amaçla, kullanıcıya parametre girme ve seçim yapma alışkanlığı kazandırır.

2.  **Tek Betik Mimarisi (`scraper.py`):**
    *   **Karar:** Proje tek bir Python betiği ile devam edecek.
    *   **Gerekçe:** Basitlik ve takip kolaylığı.

3.  **Statik Seçiciler:**
    *   **Karar:** CSS seçiciler örnek olarak bırakıldı, farklı siteler için güncellenmesi gerektiği belirtildi.
    *   **Gerekçe:** Eğitimsel amaçla, kullanıcıya HTML analizinin önemini göstermek.

4.  **Hata Durumunda Demo Veri:**
    *   **Karar:** Web sitesinden veri çekilemezse demo veri gösterilecek.
    *   **Gerekçe:** Kodun kırılgan olmaması ve her durumda çalışır örnek sunması.

## Öğrenilenler ve İçgörüler

- Kullanıcıdan parametre almak, kodun gerçek dünyadaki esnekliğini artırır.
- Bellek Bankası güncellemeleri, yapılan değişikliklerin nedenini ve etkisini netleştirir.

## Stratejik Sonraki Yön

1.  **Yapılandırma Dosyası:** URL ve CSS seçicilerini kod dışına almak.
2.  **Daha Fazla Veri Alanı:** Ürün puanı, yorum sayısı, resim URL'si gibi ek veri alanları eklemek.
3.  **Çıktı Formatları:** Sonuçları CSV veya JSON olarak kaydetme seçeneği eklemek.
