import requests
from bs4 import BeautifulSoup
import usedcars_rodmuesong_data

keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์

#webเนื้อหาดี แต่ภาษาในกาเขียนเว็บทำให้เก็บข้อมูลยาก(มาก)
def getPage():
    print("Start getPage")
    url_to_scrape = 'http://www.rod-dd.com/CarSearch.php?page=1' #website
    r = requests.get(url_to_scrape)
    soup = BeautifulSoup(r.text, "lxml")
    wikitables = soup.findAll("td")

    print(wikitables)
    #num_car = soup.select("td tr") #จำนวนรถทั้งหมด
    #print(num_car)
    #for i in num_car: #ลูปหาจำนวนหน้ามากที่สุด
        #k = i.text.strip().split(" ")
        #k = k[1].replace(",","")
    #maxpage = (int(k)//10)+1
    #print(maxpage)
    print("End getPage")
    #return maxpage

def getLink(kept):
    print("Start getLink")
    num=190
    j=0
    while(num != 5001):
        print("page "+str(num))
        url_num = 'https://rodmuesong.com/รถสำหรับขาย/p'+str(num)+''
        r = requests.get(url_num)
        soup = BeautifulSoup(r.text, "lxml")
        url_linkcar = soup.select("div.content-page div.row div.thumb-img a") #linkของรถแต่ละคัน
        for i in url_linkcar:
            print("link "+str(j+1)+i['href'])
            keep_sendlink.append('https://rodmuesong.com'+i['href'])
            j+=1
        num+=1
    print("End getLink")

def getSendLink():

    #getLink(getPage())
    j=0
    backup=[]

    for i in keep_sendlink:
        print("Link car No. "+ str(j+1) + " " + str(i))
        r = requests.get(str(i))
        soup = BeautifulSoup(r.text, "lxml")
        detail = soup.select("div.title h4.fweight-bold")
        print(detail)
        for i in detail:
            backup.append(i.text.strip())
            if(backup[0] == "OOPS! 404"):
                print(backup[0])
                continue
        usedcars_rodmuesong_data.Main(i)
        j+=1
    print("End Rod-dd")

print("Start Rod-dd")
#getSendLink()
getPage()
