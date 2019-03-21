import requests
from bs4 import BeautifulSoup
import usedcars_rodban_data
keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์
url_to_scrape = 'https://xn--22caobb7fvah1fc9id1dce1ti4me.net/Search.php?&page=1' #website
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text, "lxml")
url_linkcar = soup.select("ul.catalog_table li a") #linkของรถแต่ละคัน
num_allcar = soup.select("h2.btn8 span.comment") #จำนวนรถทั้งหมด
for i in num_allcar: #ลูปหาจำนวนหน้ามากที่สุด
    k = i.text.strip()
    k = k[0]+k[1]+k[3]+k[4]+k[5]
maxpage = (int(k)//20)+1

num=1
while(num != maxpage):
    url_to_scrape = 'https://xn--22caobb7fvah1fc9id1dce1ti4me.net/Search.php?&page='+str(num)+''
    r = requests.get(url_to_scrape)
    soup = BeautifulSoup(r.text, "lxml")
    url_linkcar = soup.select("ul.catalog_table li a")
    for i in url_linkcar:
        keep_sendlink.append(i['href'])
for i in keep_sendlink:
    usedcars_rodban_data.Main(i)

#loop check
#for i in url_linkcar:
#   print("http://www.thaicar.com"+i['href'])
#for i in num_allcar:
#    print(i.text.strip().split(" "))
