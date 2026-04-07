# 📚 Profesyonel Web Scraper & Veri Analiz Aracı

Bu uygulama, 'books.toscrape.com' e-ticaret sitesi üzerinden kitap isimlerini, fiyatlarını ve stok durumlarını otomatik olarak çeker ve analiz edilebilir bir **Excel (CSV)** raporuna dönüştürür.

## 🛠️ Teknik Yetenekler
- **HTML Parsing:** `BeautifulSoup4` ile karmaşık HTML yapılarının çözümlenmesi.
- **Veri Raporlama:** Çekilen verilerin `csv` formatında kalıcı hale getirilmesi.
- **Bot Güvenliği:** `User-Agent` başlıkları kullanılarak gerçek kullanıcı simülasyonu.
- **Hata Yönetimi:** Siteye ulaşılamaması durumunda sistemin güvenli şekilde hata vermesi.

## 📦 Kurulum
1. Projeyi indirin.
2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
