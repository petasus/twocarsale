import requests
from bs4 import BeautifulSoup
import usedcars_rodban_data

keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์

def getPage():
    print("Start getPage")
    url_to_scrape = 'https://xn--22caobb7fvah1fc9id1dce1ti4me.net/Search.php?&page=1' #website
    r = requests.get(url_to_scrape)
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
    num=1
    j=0
    while(num != kept):
        print("page "+str(num))
        url_num = 'https://xn--22caobb7fvah1fc9id1dce1ti4me.net/Search.php?&page='+str(num)+''
        r = requests.get(url_num)
        soup = BeautifulSoup(r.text, "lxml")
        url_linkcar = soup.select("div.title_box a") #linkของรถแต่ละคัน
        for i in url_linkcar:
            print("link "+str(j+1))
            keep_sendlink.append(i['href'])
            j+=1
        num+=1
    print("End getLink")

def getSendLink():

    getLink(getPage())
    j=0
    for i in keep_sendlink:
        print("Link car No. "+ str(j+1) + " " + str(i))
        usedcars_rodban_data.Main(i)
        j+=1

print("Start Rodban")
getSendLink()
