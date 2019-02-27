import requests
from bs4 import BeautifulSoup
import usedcars_thaicar_data
keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์
url_to_scrape = 'http://www.thaicar.com/car?page=1' #website
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text, "lxml")
url_linkcar = soup.select("h2.card-title a") #linkของรถแต่ละคัน
num_allcar = soup.select("h1.listing-title") #จำนวนรถทั้งหมด
for i in num_allcar: #ลูปหาจำนวนหน้ามากที่สุด
    k=i.text.strip().split(" ")
    k=k[2]
    k=k[0]+k[1]+k[3]+k[4]+k[5]
maxpage=int(k)//24

num=1
while(num != maxpage):
    url_to_scrape = 'http://www.thaicar.com/car?page='+str(num)+''
    r = requests.get(url_to_scrape)
    soup = BeautifulSoup(r.text, "lxml")
    url_linkcar = soup.select("h2.card-title a")
    num_allcar = soup.select("h1.listing-title")
    for i in url_linkcar:
        keep_sendlink.append("http://www.thaicar.com"+i['href'])
for i in keep_sendlink:
    usedcars_thaicar_data.Main(i)

#loop check
#for i in url_linkcar:
#   print("http://www.thaicar.com"+i['href']))
#for i in num_allcar:
#    print(i.text.strip().split(" "))
#for i in url_linkcar:
#    print(i['href'])
