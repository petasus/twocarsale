import requests
from bs4 import BeautifulSoup
import test_one2car_data

keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์

def getPage():
    print("Start getPage")
    url_to_scrape = 'https://www.one2car.com/%E0%B8%A3%E0%B8%96-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A-%E0%B8%82%E0%B8%B2%E0%B8%A2?type=used&page_number=1&page_size=25' #website
    r = requests.get(url_to_scrape)
    soup = BeautifulSoup(r.text, "lxml")
    num_car = soup.select("div.masthead div.flexbox__item h1.headline") #จำนวนรถทั้งหมด
    j=0
    backup=[]
    for i in num_car:
        backup = i.text.strip().split(' ')
        j=j+1
    bu = backup[2].replace(",","")
    print(bu)
    maxpage = (int(bu)//25)+1
    print(maxpage)
    print("End getPage")
    return maxpage

def getLink(kept):
    print("Start getLink")
    num=1
    j=0
    while(num != kept):
        print("page "+str(num))
        url_num = 'https://www.one2car.com/%E0%B8%A3%E0%B8%96-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A-%E0%B8%82%E0%B8%B2%E0%B8%A2?type=used&page_number='+str(num)+'&page_size=25'
        r = requests.get(url_num)
        soup = BeautifulSoup(r.text, "lxml")
        url_linkcar = soup.select("h2.listing__title a.ellipsize") #linkของรถแต่ละคัน
        for i in url_linkcar:
            print("link "+str(j+1))
            print(i)
            keep_sendlink.append(i['href'])
            j+=1
        num+=1
    print("End getLink")

def getSendLink():

    getLink(getPage())
    j=0
    for i in keep_sendlink:
        print("Link car No. "+ str(j) + " " + str(i))
        test_one2car_data.Main(i)
        j+=1

print("Start One2car")
getSendLink()
print("End One2car")
