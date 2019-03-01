import requests
from bs4 import BeautifulSoup
import usedcars_justcar_datahome
keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์
url_to_scrape = 'https://www.justcar.co.th/home?page=1' #website
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text, "lxml")
url_linkcar = soup.select("div.card-body a") #linkของรถแต่ละคัน

num=1
while(num != 6):
    url_to_scrape = 'https://www.justcar.co.th/home?page='+str(num)+''
    r = requests.get(url_to_scrape)
    soup = BeautifulSoup(r.text, "lxml")
    url_linkcar = soup.select("div.card-body a")
    for i in url_linkcar:
        keep_sendlink.append(i['href'])
for i in keep_sendlink:
    usedcars_justcar_datahome.Main(i)

#loop check
#for i in url_linkcar:
#    print(i['href'])
#for i in num_allcar:
#    print(i.text.strip().split(" "))
#for i in url_linkcar:
#    print(i['href'])
