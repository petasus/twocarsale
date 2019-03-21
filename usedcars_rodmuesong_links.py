import requests
from bs4 import BeautifulSoup
import usedcars_rodmuesong_data

keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์
url_to_scrape = 'https://rodmuesong.com/รถสำหรับขาย/p1' #website
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text, "lxml")
url_linkcar = soup.select("div.content-page div.row div.thumb-img a") #linkของรถแต่ละคัน
num_allcar = soup.select("span.result") #จำนวนรถทั้งหมด
for i in num_allcar: #ลูปหาจำนวนหน้ามากที่สุด
    k = i.text.strip().split(" ")
    k = k[1].replace(",","")
maxpage = (int(k)//10)+1

num=1
while(num != maxpage):
    url_to_scrape = 'https://rodmuesong.com/รถสำหรับขาย/p'+str(num)+''
    r = requests.get(url_to_scrape)
    soup = BeautifulSoup(r.text, "lxml")
    url_linkcar = soup.select("div.content-page div.row div.thumb-img a")
    for i in url_linkcar:
        keep_sendlink.append('https://rodmuesong.com'+i['href'])
for i in keep_sendlink:
    usedcars_rodmuesong_data.Main(i)

#loop check
#for i in url_linkcar:
    #print('https://rodmuesong.com'+i['href'])
#for i in num_allcar:
    #print(i.text.strip().split(" "))
