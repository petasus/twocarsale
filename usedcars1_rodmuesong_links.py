import requests
from bs4 import BeautifulSoup
import usedcars1_rodmuesong
import time
keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์
def getPage():
    print("Start getPage")
    url_to_scrape = 'https://rodmuesong.com/รถสำหรับขาย/p1' #website
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
    num_car = soup.select("span.result") #จำนวนรถทั้งหมด
    for i in num_car: #ลูปหาจำนวนหน้ามากที่สุด
        k = i.text.strip().split(" ")
        k = k[1].replace(",","")
    maxpage = (int(k)//10)+1
    print(maxpage)
    print("End getPage")
    return maxpage

def getLink(kept):
    print("Start getLink")
    count=kept+1    #12479
    count2=10000+1
    num=10000
    j=0
    while(num != count):
        print("page "+str(num))
        url_num = 'https://rodmuesong.com/รถสำหรับขาย/p'+str(num)+''
        while True:
            try:
                r = requests.get(url_num)
                break
            except:
                print("มีปัญหากลับไปรีเควสใหม่")
                print("ที่ลิ้ง: "+str(url_num))
                time.sleep(9)
                continue
        soup = BeautifulSoup(r.text,"lxml")
        url_linkcar = soup.select("div.content-page div.row div.thumb-img a") #linkของรถแต่ละคัน
        for i in url_linkcar:
            print("link "+str(j+1)+i['href'])
            keep_sendlink.append('https://rodmuesong.com'+i['href'])
            j+=1
        num+=1
    print("End getLink")

def getSendLink():
    print("Start Rodmuesong")
    getLink(getPage())
    print("Start getSendLink")
    usedcars1_rodmuesong.Main(keep_sendlink)
    print("End getSendLink")
    print("End Rodmuesong")

getSendLink()
