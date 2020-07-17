import requests
from bs4 import BeautifulSoup

a = int(input("Kaç tane telefon sıralamak istersiniz: "))


url = "https://www.n11.com/telefon-ve-aksesuarlari/cep-telefonu"

html = requests.get(url).content

soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("li",{"class":"column"},limit = a)

for li in list:
    name = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    oldprice = li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL")
    newprice = li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip("TL")

    print(f"name: {name} link:{link} eski fiyat:{oldprice} yeni fiyat: {newprice}")

