import requests
from bs4 import BeautifulSoup
import usedcars_rodmuesong_data

keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์

def getPage():
    print("Start getPage")
    url_to_scrape = 'https://rodmuesong.com/รถสำหรับขาย/p1' #website
    r = requests.get(url_to_scrape)
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
    num=6
    j=0
    while(num != 21):
        print("page "+str(num))
        url_to_scrape = 'https://rodmuesong.com/รถสำหรับขาย/p'+str(num)+''
        r = requests.get(url_to_scrape)
        soup = BeautifulSoup(r.text, "lxml")
        url_linkcar = soup.select("div.content-page div.row div.thumb-img a") #linkของรถแต่ละคัน
        for i in url_linkcar:
            print("link "+str(j+1))
            keep_sendlink.append('https://rodmuesong.com'+i['href'])
            j+=1
        num+=1
    print("End getLink")

def getSendLink():

    getLink(getPage())
    j=0
    for i in keep_sendlink:
        print("Link car No. "+ str(j) + " " + str(i))
        usedcars_rodmuesong_data.Main(i)
        j+=1

print("Start Rodban")
getSendLink()
