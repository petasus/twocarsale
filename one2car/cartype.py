import requests
from bs4 import BeautifulSoup
def funcsendcardt(csend):
    car_type=[]
    url_to_scrape = csend
    r = requests.get(url_to_scrape)
    soup = BeautifulSoup(r.text, "lxml")
    data=soup.select("div.listing__key-listing__list span.float--right")
    for i in data:
                car_type.append(i.text)
    for i in car_type:
        print(i)
