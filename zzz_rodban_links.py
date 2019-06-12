import requests
from bs4 import BeautifulSoup
import zzz_rodban_data
import time
keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์
#เบอร์โทรonclick
def getPage():
    print("Start getPage")
    url_to_scrape = 'https://xn--22caobb7fvah1fc9id1dce1ti4me.net/Search.php?&page=1' #website
    while True:
            try:
                r = requests.get(url_to_scrape)
                break
            except:
                print("มีปัญหากลับไปรีเควสใหม่")
                print("ที่ลิ้ง: "+str(url_to_scrape))
                time.sleep(8)
                continue
    soup = BeautifulSoup(r.text, "lxml")
    num_car = soup.select("h2.btn8 span.comment") #จำนวนรถทั้งหมด
    for i in num_car: #ลูปหาจำนวนหน้ามากที่สุด
        k = i.text.strip()
        k = k[0]+k[1]+k[3]+k[4]+k[5]
    maxpage = (int(k)//20)+1
    print(maxpage)
    print("End getPage")
    return maxpage

def getLink(kept):
    print("Start getLink")
    count=kept+1 #3407
    count2=500+1
    num=1
    j=0
    while(num != count2):
        print("page "+str(num))
        url_num = 'https://xn--22caobb7fvah1fc9id1dce1ti4me.net/Search.php?&page='+str(num)+''
        while True:
            try:
                r = requests.get(url_num)
                break
            except:
                print("มีปัญหากลับไปรีเควสใหม่")
                print("ที่ลิ้ง: "+str(url_num))
                time.sleep(9)
                continue
        soup = BeautifulSoup(r.text, "lxml")
        url_linkcar = soup.select("ul.catalog_table li h4 a") #linkของรถแต่ละคัน
        for i in url_linkcar:
            print("link "+str(j+1)+i['href'])
            keep_sendlink.append('https://xn--22caobb7fvah1fc9id1dce1ti4me.net'+ i['href'])
            j+=1
        num+=1
    print("End getLink")

def getSendLink():
    print("Start Rodban")
    getLink(getPage())
    print("Start getSendLink")
    zzz_rodban_data.Main(keep_sendlink)
    print("End getSendLink")
    print("End Rodban")

getSendLink()
