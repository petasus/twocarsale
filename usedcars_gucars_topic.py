import requests
from bs4 import BeautifulSoup
import usedcars_gucars_cardata
keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์
url_to_scrape = 'https://gucars.com/search/used-car?page=1' #website
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text, "lxml")
url_linkcar = soup.select("div.box a") #linkของรถแต่ละคัน
num_allcar = soup.select("span.c-font-16") #จำนวนรถทั้งหมด
for i in num_allcar: #ลูปหาจำนวนหน้ามากที่สุด
    k=i.text.strip().split(" ")
    k=k[1]
maxpage=int(k)//20
num=1
while(num != maxpage):
    url_to_scrape = 'https://gucars.com/search/used-car?page='+str(num)+''
    r = requests.get(url_to_scrape)
    soup = BeautifulSoup(r.text, "lxml")
    url_linkcar = soup.select("div.box a")
    num_allcar = soup.select("span.c-font-16")
    for i in url_linkcar:
        keep_sendlink.append(i['href'])
for i in keep_sendlink:
    usedcars_gucars_cardata.Main(i)
#loop check
#for i in url_linkcar:
#    print(i['href'])
#for i in num_allcar:
#    print(i.text.strip().split(" "))
#for i in url_linkcar:
#    print(i['href'])
