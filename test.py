import requests
from bs4 import BeautifulSoup
import time
ktl=[]
ktt=[]
ktn=[]
def getLink():
    url_to_type = 'https://chobrod.com/car-sale/p1' #website
    r = requests.get(url_to_type)
    soups = BeautifulSoup(r.text, "lxml")
    type_name = soups.select("div.item span")
    for i in type_name:
        #print(i.text.strip())
        ktn.append(i.text.strip())
    print(ktn)

getLink()
