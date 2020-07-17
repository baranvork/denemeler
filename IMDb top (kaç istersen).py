import requests
from bs4 import BeautifulSoup

a = int(input("Kaç tane sıralamak istersin: "))

url = "https://www.imdb.com/chart/top/"

html = requests.get(url).content

soup = BeautifulSoup(html,"html.parser")

list = soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit = a)
count = 1
for tr in list:
    title  = tr.find("td",{"class":"titleColumn"}).find("a").text
    year = tr.find("td",{"class":"titleColumn"}).find("span").text
    rate = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    print(f"{count}- film:{title.ljust(60)} yıl: {year}  değerlendirme: {rate}")
    count  +=1






