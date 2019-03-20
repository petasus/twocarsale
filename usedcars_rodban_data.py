import requests
from bs4 import BeautifulSoup

def get_Price(soup): #ราคา
    detail = soup.select("div.car_characteristics div.price")
    j=0
    backup=[]
    for i in detail:
        backup = i.text.strip().split(' ')
        j=j+1
    bu = backup[1]
    bu1 = bu.replace("บาท","")
    bu2 = bu1.replace(",","")
    bu3 = bu2.replace("\t","")
    #print(int(bu3))

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    bu = ("รถ"+backup[0][0])
    bu1 = bu.replace(" ","")
    if(bu1=="แวน"):
        bu2 = "รถมินิแวน"
        #print(bu2)
    else:
        bu2 = bu1
        #print(bu2)

def get_Brand(soup): #ยี่ห้อ
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        backup2=backup[0][1].split('\t')
        j=j+1
    bu = backup2[1]
    bu1 = bu.replace(",","")
    bu2 = bu1.replace(" ","")
    bu3 = (bu2.lower())
    #print(bu3)

def get_Model(soup): #รุ่น
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        backup2=backup[0][2].split('\t')
        j=j+1
    bu = backup2[1]
    bu1 = bu.replace(",","")
    bu2 = bu1.replace(" ","")
    bu3 = (bu2.lower())
    #print(bu3)

def get_Year(soup): #รุ่นปี
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        backup2=backup[0][7]
        j=j+1
    bu = backup2
    bu1 = bu.replace("ปี","")
    bu2 = bu1.replace("\t","")
    bu3 = bu2.replace(":","")
    bu4 = bu3.replace(" ","")
    #print(bu4)

def get_Color(soup): #สีรถ
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print("สี"+backup[5])

def get_Engine(soup): #ขนาดเครื่องยนต์
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[6]
    bu1 = bu.replace(",","")
    bu2 = bu1.replace(" ","")
    bu3 = bu2.replace("CC","")
    #print(bu3)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[4]
    bu1 = bu.replace("ออโต้","")
    bu2 = bu1.replace("ธรรมดา","")
    bu3 = bu2.replace("/","")
    bu4 = bu3.replace(" ","")
    if(bu4 == "manual"):
        bu5 = "เกียร์ธรรมดา"
        #print(bu5)
    elif(bu4 == "Automatic"):
        bu5 = "เกียร์อัตโนมัติ"
        #print(bu5)

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[3]
    bu1 = bu.replace("km","")
    bu2 = bu1.replace("-","")
    bu3 = bu2.replace(",","")
    bu4 = bu3.replace(" ","")
    bu5 = bu4[0]+bu4[1]+bu4[2]+bu4[3]+bu4[4]
    bu6 = bu4[5]+bu4[6]+bu4[7]+bu4[8]+bu4[9]
    bu7 = (int(bu5)+int(bu6))/2
    #print(bu7)

def get_SellName(soup): #ชื่อผู้ขาย
    detail = soup.select("div.author span a")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup[0])

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("div.phones div.pointer")
    j=0
    backup=[]
    for i in detail:
        backup.append(i)
        j=j+1
    bu = str(backup)
    bu1 = bu[65]+bu[66]+bu[67]+bu[68]+bu[69]+bu[70]+bu[71]+bu[72]+bu[73]+bu[74]
    #print(bu1)

def get_Location(soup): #จังหวัด
    detail = soup.select("div.right a")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = (backup[5])
    bu1 = bu.replace(" ","")
    #print(bu1)

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[7].split(" ")
    dd = bu[0]
    mm = bu[1]
    yy = bu[2].replace(",","")

    months = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
    for i in months:
        if i == mm:
            mm = str(months.index(i)+1)

    fulldate = (yy +'-'+ mm +'-'+ dd)
    print (fulldate)

def Main(links):
    r = requests.get(links)
    soup = BeautifulSoup(r.text, "lxml")
    cars_detail = []
    CarDetail = {}
    CarDetail['pri'] = get_Price(soup)
    CarDetail['typ'] = get_TypeCar(soup)
    CarDetail['bnd'] = get_Brand(soup)
    CarDetail['mod'] = get_Model(soup)
    CarDetail['yea'] = get_Year(soup)
    CarDetail['col'] = get_Color(soup)
    CarDetail['eng'] = get_Engine(soup)
    CarDetail['gea'] = get_Gear(soup)
    CarDetail['mil'] = get_Mileage(soup)
    CarDetail['sel'] = get_SellName(soup)
    CarDetail['tel'] = get_SellTel(soup)
    CarDetail['loc'] = get_Location(soup)
    CarDetail['dat'] = get_Date(soup)

Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/toyotacamry-138983.html')
