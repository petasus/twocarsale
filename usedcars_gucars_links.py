import requests
from bs4 import BeautifulSoup
import usedcars_gucars_data

keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์

def getPage():
    print("Start getPage")
    url_to_scrape = 'https://gucars.com/search/used-car?page=1' #website
    r = requests.get(url_to_scrape)
    soup = BeautifulSoup(r.text, "lxml")
    num_car = soup.select("span.c-font-16") #จำนวนรถทั้งหมด
    for i in num_car: #ลูปหาจำนวนหน้ามากที่สุด
        k = i.text.strip().split(" ")
        k = k[1]
    maxpage = (int(k)//20)+1 #จำนวนรถหารด้วยจำนวนรถที่แสดงใน1หน้า
    print(maxpage)
    print("End getPage")
    return maxpage

def getLink(kept):
    print("Start getLink")
    num=kept
    j=0
    while(num != 1872):
        print("page "+str(num))
        url_num = 'https://gucars.com/search/used-car?page='+str(num)+''
        r = requests.get(url_num)
        soup = BeautifulSoup(r.text, "lxml")
        url_linkcar = soup.select("div.box a") #linkของรถแต่ละคัน
        for i in url_linkcar:
            print("link "+str(j+1))
            keep_sendlink.append(i['href'])
            j+=1
        num-=1
    print("End getLink")

def getSendLink():

    getLink(getPage())
    j=0
    for i in keep_sendlink:
        print("Link car No. "+ str(j+1) + " " + str(i))
        #usedcars_gucars_data.Main(i)
        j+=1

print("Start Gucars")
getSendLink()
