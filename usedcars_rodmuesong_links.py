import requests
from bs4 import BeautifulSoup
import usedcars_rodmuesong_data

keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์

def getPage():
    url_to_scrape = 'https://rodmuesong.com/รถสำหรับขาย/p1' #website
    r = requests.get(url_to_scrape)
    soup = BeautifulSoup(r.text, "lxml")
    num_allcar = soup.select("span.result") #จำนวนรถทั้งหมด
    for i in num_allcar: #ลูปหาจำนวนหน้ามากที่สุด
        k = i.text.strip().split(" ")
        k = k[1].replace(",","")
    maxpage = (int(k)//10)+1
    return maxpage

def getKeeplink(kept):
    num=1
    while(num != kept):
        url_to_scrape = 'https://rodmuesong.com/รถสำหรับขาย/p'+str(num)+''
        r = requests.get(url_to_scrape)
        soup = BeautifulSoup(r.text, "lxml")
        url_linkcar = soup.select("div.content-page div.row div.thumb-img a") #linkของรถแต่ละคัน
        for i in url_linkcar:
            keep_sendlink.append('https://rodmuesong.com'+i['href'])
        num+=1


def getSendLink():

    getKeeplink(getPage())

    for i in keep_sendlink:
        usedcars_rodmuesong_data.Main(i)

getSendLink()
