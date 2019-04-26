import requests
from bs4 import BeautifulSoup
import tested_traderod_data

keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์

#ขาดประเภทรถ มีสีภาษาอังกฤษปนมา
def getLink():
    print("Start getLink")
    count=0
    num=1
    j=0
    while(num != count):
        print("page "+str(num))
        url_num = 'https://www.traderod.com/cars/index.php?pg='+str(num)+'&sortyear=DESC&main_cate=&brand_car=&model_car=&version_car=&year_car=&detail_car=&start_price=&end_price=&submodel_car='
        r = requests.get(url_num)
        soup = BeautifulSoup(r.text, "lxml")
        url_linkcar = soup.select("div.col-sm-6 div.box_carpost a") #linkของรถแต่ละคัน
        for i in url_linkcar:
            print("link "+str(j+1)+i['href'])
            keep_sendlink.append(i['href'])
            j+=1
        num+=1
        detail = soup.select("div.col-sm-12 h2.red")
        if(detail == "ต่ำกว่าปี 1980"):
            num=0
    print("End getLink")

def getSendLink():
    print("Start getSendLink")
    getLink()

    tested_traderod_data.Main(keep_sendlink)
    #tested_traderod_data.Testl(keep_sendlink)#test

    print("End getSendLink")
    print("End Traderod")

print("Start Traderod")
getSendLink()

