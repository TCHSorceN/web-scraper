import requests
from bs4 import BeautifulSoup
import csv


def profesyonel_scraper():
    url = "http://books.toscrape.com/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        cevap = requests.get(url, headers=headers)
        cevap.encoding = 'utf-8'
        soup = BeautifulSoup(cevap.text, 'html.parser')

        kitaplar = soup.find_all("article", class_="product_pod")

        kitap_listesi = []

        for kitap in kitaplar:
            baslik = kitap.h3.a["title"]
            fiyat = kitap.find("p", class_="price_color").text
            stok = kitap.find("p", class_="instock availability").text.strip()

            kitap_listesi.append({
                "Kitap Adı": baslik,
                "Fiyat": fiyat,
                "Stok Durumu": stok
            })

        alanlar = ["Kitap Adı", "Fiyat", "Stok Durumu"]
        with open("kitap_raporu.csv", "w", newline="", encoding="utf-8") as dosya:
            yazici = csv.DictWriter(dosya, fieldnames=alanlar)
            yazici.writeheader()
            yazici.writerows(kitap_listesi)

        print(f"✅ İşlem Başarılı! {len(kitap_listesi)} kitap çekildi ve 'kitap_raporu.csv' dosyasına kaydedildi.")

    except Exception as hata:
        print(f"❌ Kritik Hata: {hata}")


profesyonel_scraper()