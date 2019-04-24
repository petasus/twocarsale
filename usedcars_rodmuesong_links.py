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
    j=0
    backup=[]
    count = kept+1
    num=1
    j=0
    while(num != count):
        print("page "+str(num))
        url_num = 'https://rodmuesong.com/รถสำหรับขาย/p'+str(num)+''
        r = requests.get(url_num)
        soup = BeautifulSoup(r.text, "lxml")
        url_linkcar = soup.select("div.content-page div.row div.thumb-img a") #linkของรถแต่ละคัน
        for i in url_linkcar:
            print("link "+str(j+1)+i['href'])
            rs = requests.get(str(i))
            soups = BeautifulSoup(rs.text, "lxml")
            detail = soups.select("div.title h4.fweight-bold")
            #print(detail)
            for i in detail:
                backup.append(i.text.strip())
            if(backup[0] == "OOPS! 404"):
                continue
            keep_sendlink.append('https://rodmuesong.com'+i['href'])
            j+=1
        num+=1
    print("End getLink")

def getSendLink():
    print("Start getSendLink")
    #getLink(100)
    getLink(getPage())

    usedcars_rodmuesong_data.Main(keep_sendlink)

    print("End getSendLink")
    print("End Rodmuesong")

#def M(test):
#    back=[]
#    num=0
#    j=0
#    while(num!=1):
#        print(str(num) + " " + test)
#        keep_sendlink.append(test)
#        r = requests.get(test)
#        soup = BeautifulSoup(r.text, "lxml")
#        detail = soup.select("div.title h4.fweight-bold")
#        print(detail)
#        for i in detail:
#            back.append(i.text.strip())
#            print("^^")
#            print(back)
#            print("**")
#            print(back[0])
#            if(back[0] == "OOPS! 404"):
#                print(back[0])
#                continue
#            else:
#                usedcars_rodmuesong_data.Main(i)
#        num+=1
#M('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/chevrolet-colorado-year-2011/%E0%B8%82%E0%B8%B2%E0%B8%A2%E0%B8%A3%E0%B8%96-%E0%B8%97%E0%B8%B5%E0%B9%88-%E0%B8%8A%E0%B8%A5%E0%B8%9A%E0%B8%B8%E0%B8%A3%E0%B8%B5-aid7097521')
#M('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/ford-fiesta-year-2012/2012-%E0%B8%AA%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B8%94%E0%B8%B5-aid7135721')
#M('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/bmw-series-3-year-2017/%E0%B8%82%E0%B8%B2%E0%B8%A2%E0%B8%A3%E0%B8%96-%E0%B8%97%E0%B8%B5%E0%B9%88-%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A3-aid7224731')
#M('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/bmw-x1-sdrive18i-year-2013/%E0%B8%82%E0%B8%B2%E0%B8%A2%E0%B8%A3%E0%B8%96-2013-%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%A7%E0%B8%A2%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%94%E0%B8%B5-aid7227941')
#M('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/toyota-fortuner-year-2014/%E0%B8%82%E0%B8%B2%E0%B8%A2%E0%B8%A3%E0%B8%96-%E0%B8%97%E0%B8%B5%E0%B9%88-%E0%B8%AA%E0%B8%A1%E0%B8%B8%E0%B8%97%E0%B8%A3%E0%B8%9B%E0%B8%A3%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3-aid7302691')
#M('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/mitsubishi--year-1995/%E0%B8%82%E0%B8%B2%E0%B8%A2%E0%B8%A3%E0%B8%96-%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%E0%B8%AD%E0%B8%B7%E0%B9%88%E0%B8%99%E0%B9%86-%E0%B8%97%E0%B8%B5%E0%B9%88-%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A3-aid7302341')
#M('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/toyota-corolla-year-2014/2014-%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%94%E0%B8%B5-aid7272321')
#M('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/isuzu-d-max-year-2004/2004-%E0%B8%AA%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B8%94%E0%B8%B5-aid7274281')
#M('https://rodmuesong.com/รถสำหรับขาย/honda-civic-year-1998/ราคาถูก-aid7315641')
#M('https://rodmuesong.com/รถสำหรับขาย/mitsubishi-space-wagon-gt-year-2008/2008-รับประกันใช้ดี-aid7407051')

print("Start Rodmuesong")
getSendLink()

