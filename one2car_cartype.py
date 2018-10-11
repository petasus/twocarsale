import requests
from bs4 import BeautifulSoup
import one2car_datacar
data_keeplink=[]
url_to_scrape = 'https://www.one2car.com/%E0%B8%A3%E0%B8%96-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A-%E0%B8%82%E0%B8%B2%E0%B8%A2?type=used&page_number=1&page_size=25'
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text, "lxml")
data_linkcar = soup.select("a.ellipsize")
data_numallcar = soup.select("h1.headline.delta.flush")
for i in data_numallcar:
    k=i.text.strip().split(" ")
    k=k[2]
    k=k.strip().split(",")
    k=k[0]+k[1]
maxpage=int(k)//25

num=1
while(num != maxpage):
    url_to_scrape = 'https://www.one2car.com/%E0%B8%A3%E0%B8%96-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A-%E0%B8%82%E0%B8%B2%E0%B8%A2?type=used&page_number='+str(num)+'&page_size=25'
    r = requests.get(url_to_scrape)
    soup = BeautifulSoup(r.text, "lxml")
    data_linkcar = soup.select("a.ellipsize")
    data_numallcar = soup.select("h1.headline.delta.flush")
    for i in data_linkcar:
        data_keeplink.append(i['href'])

for i in data_keeplink:
    one2car_datacar.sendlinks(i)


