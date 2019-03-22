import requests
from bs4 import BeautifulSoup
import usedcars_gucars_data

keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์

def getPage():
    print("Start getPage")
    url_to_scrape = 'https://gucars.com/search/used-car?page=1' #website
    r = requests.get(url_to_scrape)
    soup = BeautifulSoup(r.text, "lxml")
    num_allcar = soup.select("span.c-font-16") #จำนวนรถทั้งหมด
    print("in loop")
    for i in num_allcar: #ลูปหาจำนวนหน้ามากที่สุด
        k = i.text.strip().split(" ")
        print(k)
        k = k[1]
    print(k)
    maxpage = (int(k)//20)+1 #จำนวนรถหารด้วยจำนวนรถที่แสดงใน1หน้า
    print(maxpage)
    print("End getPage")
    return maxpage

def getKeeplink(kept):
    print("Start getKeeplink")
    j=0
    num=1
    while(num != 3):
        url_to_scrape = 'https://gucars.com/search/used-car?page='+str(num)+''
        print(url_to_scrape)
        r = requests.get(url_to_scrape)
        soup = BeautifulSoup(r.text, "lxml")
        url_linkcar = soup.select("div.box a") #linkของรถแต่ละคัน

        print("in loop"+str(num))
        for i in url_linkcar:
            keep_sendlink.append(i['href'])
            print("ลิ้งที่ทำอยู่ "+str(j+1)+" "+keep_sendlink[j])
            j+=1
        num+=1
        url_linkcar=[]
    print("End getKeeplink")

def getSendLink():

    getKeeplink(getPage())
    print("Start getSendlink")
    #for i in keep_sendlink:
    #    print("ลิ้งที่ส่งอยู่ "+i)
    #    usedcars_gucars_data.Main(i)
    print("End getSendlink")

print("Start Gucars.com")
getSendLink()
