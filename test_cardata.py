import requests
from bs4 import BeautifulSoup
import test_cartype
car_data=[]
url_to_scrape = 'https://www.one2car.com/%E0%B8%A3%E0%B8%96%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%AA%E0%B8%AD%E0%B8%87-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A-%E0%B8%82%E0%B8%B2%E0%B8%A2'
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text, "lxml")
data=soup.select("article.listing.listing--card.box.relative.push--top.js--listing.js--multi-lead div div h2 a")
for i in data:
    car_data.append(i['href'])

#for i in car_data:
#    cartype.funcsendcardt(i)
