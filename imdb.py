import requests
from bs4 import BeautifulSoup

url = "https://atilganticaret.com/urun-kategori/atilgan-ticaret-kampanya/?product_brand=renault-mais"


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html,"html.parser")

liste = soup.find("ul",{"class":"products columns-4"}).find_all("li",limit = 12)

for item in liste:
    urunadi = item.find("h2",{"class":"woo-loop-product__title"}).text
    print(urunadi)
