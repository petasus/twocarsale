import requests
from bs4 import BeautifulSoup

def get_Price(soup): #ราคา
    detail = soup.select("div.row p.font-thaisans")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        backup1=backup[0][1].split(' ')
    #print(backup1)
    bu = backup1[1]
    bu1 = bu.replace(",","")
    print(bu1)
    return(bu1)

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("div.row p.font-thaisans")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    bu=backup[1][3].split(' ')
    bu1 = bu[1]
    if(bu1 == "รถออฟโรด"):
        bu2 = "รถSUV"
    elif(bu1 == "รถหรู"):
        bu2 = "รถสปอร์ต"
    else:
        bu2 = bu1
    print(bu2)
    return(bu2)

def get_Brand(soup): #ยี่ห้อ
    detail = soup.select("div.row p.font-thaisans")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        backup1=backup[0][2].split(' ')
    bu = (backup1[1].lower())
    print(bu)
    return(bu)

def get_Model(soup): #รุ่น
    detail = soup.select("div.row p.font-thaisans")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        backup2=backup[0][3].split(' ')
    bu = (backup2[1].lower())
    print(bu)
    return(bu)

def get_Year(soup): #รุ่นปี
    detail = soup.select("div.row p.font-thaisans")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        backup2=backup[0][4].split(' ')
    bu = backup2[1]
    print(bu)
    return(bu)

def get_Color(soup): #สีรถ
    detail = soup.select("div.row p.font-thaisans")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    bu = backup[1][2].split(' ')
    print("สี"+bu[1])
    return("สี"+bu[1])

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.row p.font-thaisans")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    bu = backup[1][0].split(' ')
    if(bu[1] == "ธรรมดา"):
        bu = "เกียร์ธรรมดา"
    elif(bu[1] == "ออโต้"):
        bu = "เกียร์อัตโนมัติ"
    print(bu)
    return(bu)

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div.row p.font-thaisans")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    bu = backup[1][1].split(' ')
    if(bu[1] == '' or bu[1] == "ไม่กำหนด"):
        bu2 = "-"
    else:
        bu1 = bu[1]
        bu2 = bu1.replace(",","000")

    print(bu2)
    return(bu2)

def get_SellName(soup): #ชื่อผู้ขาย
    detail = soup.select("div.c-center p.c-font-bold")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split(' '))
        j=j+1
    if(backup == []):
        bu3 = "-"
    else:
        bu = backup[0][0]
        bu1 = backup[0][1]
        bu2 = backup[0][2]
        bu3 = bu+" "+bu1+" "+bu2
    print(bu3)
    return(bu3)

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("div.c-center a.btn")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    if(j == 2):
        bu = backup[0]
        bu1 = bu[0:10]
    else:
        bu1 = "-"
    print(bu1)
    return(bu1)

def get_Location(soup): #จังหวัด
    detail = soup.select("div.c-center p.font-thaisans")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    if(backup == []):
        bu2 = "-"
    elif(j == 2):
        bu = backup[1][1]
        bu1 = bu.replace(" ","")
        bu2 = bu1.replace(">","")
    elif(j == 3):
        bu = backup[2][1]
        bu1 = bu.replace(" ","")
        bu2 = bu1.replace(">","")
    print(bu2)
    return(bu2)

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("div.row p.font-thaisans")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    #print(backup)
    bu = backup[1][4].split(' ')
    bu1 = bu[1].split("/")
    dd = bu1[0]
    mm = int(bu1[1])
    mm1 = str(mm)
    yy = (int(bu1[2])+2543)
    yy1 = str(yy)
    fulldate = (yy1 +'-'+ mm1 +'-'+dd)
    print(fulldate)
    return(fulldate)

def Main(links):
    r = requests.get(links)
    soup = BeautifulSoup(r.text, "lxml")
    cars_detail = []
    CarDetail = {}
    CarDetail['pri'] = get_Price(soup)
    CarDetail['typ'] = get_TypeCar(soup)
    CarDetail['bra'] = get_Brand(soup)
    CarDetail['mod'] = get_Model(soup)
    CarDetail['yea'] = get_Year(soup)
    CarDetail['col'] = get_Color(soup)
    #CarDetail['eng'] = get_Engine(soup)
    CarDetail['gea'] = get_Gear(soup)
    CarDetail['mil'] = get_Mileage(soup)
    CarDetail['sel'] = get_SellName(soup)
    CarDetail['tel'] = get_SellTel(soup)
    CarDetail['loc'] = get_Location(soup)
    CarDetail['dat'] = get_Date(soup)

#Main('https://gucars.com/used-car-sale/TOYOTA-HILUX REVO-2016/47030')
#Main('https://gucars.com/used-car/TOYOTA-CAMRY-2004/1583')
#Main('https://gucars.com/used-car/TOYOTA-CAMRY-2007/46885')
#Main('https://gucars.com/used-car-sale/HONDA-CIVIC-2016/47025')
#Main('https://gucars.com/used-car-sale/HONDA-CITY-2012/47108')
