import requests
from bs4 import BeautifulSoup
import one2car_cardata
keep_sendlink=[]
url_to_scrape = 'https://www.one2car.com/%E0%B8%A3%E0%B8%96-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A-%E0%B8%82%E0%B8%B2%E0%B8%A2?type=used&page_number=1&page_size=25'
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text, "lxml")
url_linkcar = soup.select("a.ellipsize")
num_allcar = soup.select("h1.headline.delta.flush")
for i in num_allcar:
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
    url_linkcar = soup.select("a.ellipsize")
    num_allcar = soup.select("h1.headline.delta.flush")
    for i in url_linkcar:
        keep_sendlink.append(i['href'])

for i in keep_sendlink:
    one2car_cardata.Main(i)
