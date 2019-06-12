import requests
from bs4 import BeautifulSoup
import usedcars3_traderod_data
import time
keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์
#ขาดประเภทรถ มีสีภาษาอังกฤษปนมา
def getLink():
    print("Start getLink")
    count=0 #636 หน้าละ12 link
    num=1
    j=0
    k=0
    while(num != count):
        print("page "+str(num))
        url_num = 'https://www.traderod.com/cars/index.php?pg='+str(num)+'&sortyear=DESC&main_cate=&brand_car=&model_car=&version_car=&year_car=&detail_car=&start_price=&end_price=&submodel_car='
        while True:
            try:
                r = requests.get(url_num)
                break
            except:
                print("มีปัญหากลับไปรีเควสใหม่")
                print("ที่ลิ้ง: "+str(url_num))
                time.sleep(8)
                continue
        soup = BeautifulSoup(r.text, "lxml")
        url_linkcar = soup.select("div.col-sm-6 div.box_carpost a") #linkของรถแต่ละคัน
        for i in url_linkcar:
            print("link "+str(j+1)+i['href'])
            keep_sendlink.append(i['href'])
            j+=1
        num+=1
        check = soup.select("div.col-sm-12 h2.red")
        for i in check:
            bu = (i.text.strip())
        if(bu == "ต่ำกว่าปี 1980"):
            count = num+1
            k+=1
            print(k)
            if(k == 3):
                count = num
                print(count-1)
    print("End getLink")

def getSendLink():
    print("Start Traderod")
    getLink()
    print("Start getSendLink")
    usedcars3_traderod_data.Main(keep_sendlink)
    print("End getSendLink")
    print("End Traderod")

getSendLink()
