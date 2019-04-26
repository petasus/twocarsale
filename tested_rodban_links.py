import requests
from bs4 import BeautifulSoup
import tested_rodban_data

keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์

#เบอร์โทรonclick
def getPage():
    print("Start getPage")
    url_to_scrape = 'https://xn--22caobb7fvah1fc9id1dce1ti4me.net/Search.php?&page=1' #website
    r = requests.get(url_to_scrape)
    soup = BeautifulSoup(r.text, "lxml")
    num_car = soup.select("h2.btn8 span.comment") #จำนวนรถทั้งหมด
    for i in num_car: #ลูปหาจำนวนหน้ามากที่สุด
        k = i.text.strip()
        k = k[0]+k[1]+k[3]+k[4]+k[5]
    #maxpage = (int(k)//20)+1
    maxpage=10
    print(maxpage)
    print("End getPage")
    return maxpage

def getLink(kept):
    print("Start getLink")
    backup=[]
    count=kept+1
    num=1
    j=0
    while(num != count):
        print("page "+str(num))
        url_num = 'https://xn--22caobb7fvah1fc9id1dce1ti4me.net/Search.php?&page='+str(num)+''
        r = requests.get(url_num)
        soup = BeautifulSoup(r.text, "lxml")
        url_linkcar = soup.select("ul.catalog_table li h4 a") #linkของรถแต่ละคัน
        for i in url_linkcar:
            print("link "+str(j+1)+i['href'])
            rs = requests.get('https://xn--22caobb7fvah1fc9id1dce1ti4me.net'+(i['href']))
            soups = BeautifulSoup(rs.text, "lxml")
            detail = soups.select("div.catalog_desc div.title_box h4")
            for i in detail:
                backup.append(i.text.strip())
            if(backup == "ขออภัยค่ะ ! ประกาศนี้ไม่มีในระบบแล้ว"):
                    continue
            keep_sendlink.append('https://xn--22caobb7fvah1fc9id1dce1ti4me.net'+ i['href'])
            j+=1
        num+=1
    print("End getLink")

def getSendLink():
    print("Start getSendLink")
    getLink(getPage())

    #usedcars_rodban_data.Main(keep_sendlink)
    #usedcars_rodban_data.Test(keep_sendlink)#test
    print("End getSendLink")
    print("End Rodban")

print("Start Rodban")
getSendLink()
