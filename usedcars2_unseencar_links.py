import requests
from bs4 import BeautifulSoup
import usedcars2_unseencar
import time
keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์
def getPage():
    print("Start getPage")
    url_to_scrape = 'https://unseencar.com/taladrod/p1' #website
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
    num_car = soup.select("span.sp-search1") #จำนวนรถทั้งหมด
    for i in num_car: #ลูปหาจำนวนหน้ามากที่สุด
        k = i.text.strip().split(" ")
        k = k[1].replace(",","")
    maxpage = (int(k)//10)+1
    print(maxpage)
    print("End getPage")
    return maxpage

def getLink(kept):
    print("Start getLink")
    count=kept+1 #1333
    count2=20+1
    num=1
    j=0
    while(num != count):
        print("page "+str(num))
        url_num = 'https://unseencar.com/taladrod/p'+str(num)+''
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
        url_linkcar = soup.select("h3.title-20 a") #linkของรถแต่ละคัน
        for i in url_linkcar:
            print("link "+str(j+1)+i['href'])
            keep_sendlink.append('https://unseencar.com'+i['href'])
            j+=1
        num+=1
    print("End getLink")

def getSendLink():
    print("Start Unseencar")
    getLink(getPage())
    print("Start getSendLink")
    usedcars2_unseencar.Main(keep_sendlink)
    print("End getSendLink")
    print("End Unseencar")

getSendLink()
