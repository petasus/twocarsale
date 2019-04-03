import requests
from bs4 import BeautifulSoup
import test_traderod_data

keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์

def getLink():
    print("Start getLink")
    kept = 672
    num=1
    j=0
    while(num != kept):
        print("page "+str(num))
        url_num = 'https://www.traderod.com/cars/index.php?pg='+str(num)+'&sortyear=DESC&main_cate=&brand_car=&model_car=&version_car=&year_car=&detail_car=&start_price=&end_price=&submodel_car='
        r = requests.get(url_num)
        soup = BeautifulSoup(r.text, "lxml")
        url_linkcar = soup.select("div.col-sm-6 div.box_carpost a") #linkของรถแต่ละคัน
        for i in url_linkcar:
            print("link "+str(j+1))
            keep_sendlink.append(i['href'])
            j+=1
        num+=1
    print("End getLink")

def getSendLink():

    getLink()
    j=0
    for i in keep_sendlink:
        print("Link car No. "+ str(j+1) + " " + str(i))
        test_traderod_data.Main(i)
        j+=1

print("Start Traderod")
getSendLink()
print("End Traderod")
