import requests
from bs4 import BeautifulSoup
from upload_data import uploadToSql as uploadDB
from connect import conDB as database

def get_Price(soup): #ราคา
    detail = soup.select("div.left-content p.price")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu0 = backup[0]
    if(bu0 == "ติดต่อผู้ขาย"):
        bu3 = "-"
    else:
        bu = bu0
        bu1 = bu.replace("บาท","")
        bu2 = bu1.replace(",","")
        bu3 = bu2.replace(" ","")
    print(bu3)
    return(bu3)

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    for i in backup:
        if(i == "ประเภทรถ" ):
            a = k+1
        k=k+1
    if(a != 1000):
        bu = (backup[a].lower())
    else:
        bu = "-"
    if(bu == "รถเก๋ง 4 ประตู" or bu == "รถเก๋ง 5 ประตู"):
        bu1 = "รถเก๋ง"
    elif(bu == "SUV" or bu == "suv"):
        bu1 = "รถSUV"
    elif(bu == "Truck" or bu == "truck"):
        bu1 = "รถบรรทุก"
    elif(bu == "Wagon" or bu == "wagon"):
        bu1 = "รถWagon"
    elif(bu == "รถตู้/MPV" or bu == "รถตู้/mpv" or bu == "รถตู้/VAN" or bu == "รถตู้/van"):
        bu1 = "รถตู้"
    elif(bu == "รถเก๋ง 2 ประตู" or bu == "รถเปิดประทุน" or bu == "Cabriolet"):
        bu1 = "รถสปอร์ต"
    else:
        bu1 = bu
    print(bu1)

    while(True):
        CKsql = """ SELECT id FROM type_car WHERE `name`=%s"""
        CKExis = c.execute(CKsql,(bu))
        if CKExis:
            getID = CKExis.fetchall()
            return getID[0][0]
        else:
            c.execute("""INSERT INTO type_car (`name`) VALUES (%s)""", (bu))
            database.commit()
            continue

def get_Brand(soup): #ยี่ห้อ
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    for i in backup:
        if(i == "ยี่ห้อ" ):
            a = k+1
        k=k+1
    if(a != k):
        bu = (backup[a].lower())
    else:
        bu = "-"
    print(bu)

    while(True):
        CKsql = """ SELECT id FROM brand WHERE `name`=%s"""
        CKExis = c.execute(CKsql,(bu))
        if CKExis:
            getID = CKExis.fetchall()
            return getID[0][0]
        else:
            c.execute("""INSERT INTO brand (`name`) VALUES (%s)""", (bu))
            database.commit()
            continue

def get_Model(soup): #รุ่น
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    for i in backup:
        if(i == "รุ่น" ):
            a = k+1
        k=k+1
    if(a != 1000):
        bu = (backup[a].lower())
    else:
        bu = "-"
    print(bu)
    TypeCar = get_TypeCar(soup)
    Brand = get_Brand(soup)
    Gear = get_Gear(soup)
    while(True):
        CKsql = """ SELECT id FROM model WHERE `name`=%s AND 'bnd_id'=%s AND 'typ_id'=%s"""
        CKExis = c.execute(CKsql,(bu,Brand,TypeCar))
        if CKExis:
            getID = CKExis.fetchall()
            return getID[0][0]
        else:
            c.execute("""INSERT INTO type_car (`name`,`bnd_id`,`typ_id`,`gears`) VALUES (%s,%s,%s,%s)""", (bu,Brand,TypeCar,Gear))
            database.commit()
            continue

def get_Year(soup): #รุ่นปี
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    for i in backup:
        if(i == "ปีที่ผลิต" ):
            a = k+1
        k=k+1
    if(a != 1000):
        bu = backup[a]
    else:
        bu = "-"
    print(bu)
    return(bu)

def get_Color(soup): #สีรถ
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    for i in backup:
        if(i == "สี" ):
            a = k+1
        k=k+1
    if(a != 1000):
        bu = backup[a]
    else:
        bu = "-"
    print(bu)
    return(bu)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    for i in backup:
        if(i == "ระบบส่งกำลัง" ):
            a = k+1
        k=k+1
    if(a != 1000):
        bu = backup[a]
    else:
        bu = "-"
    print(bu)
    return(bu)

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    for i in backup:
        if(i == "เลขไมล์" ):
            a=k+1
        k=k+1
    if(a != 1000):
        bu = backup[a]
        bu1 = bu.replace(",","")
    else:
        bu1 = "-"
    print(bu1)
    return(bu1)

def get_SellName(soup): #ชื่อผู้ขาย
    detail = soup.select("div.col-box h4")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[0]
    if(bu == ''):
        bu1 = "-"
    else:
        bu1 = bu
    print(bu1)
    return(bu1)

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("div.col-box span")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[0].replace(".","")
    print(bu)
    return(bu)

def get_Location(soup): #จังหวัด
    detail = soup.select("div.title-page p.info-title")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[0].replace("|","")
    bu1 = bu.split(" ")
    bu2 = bu1[0]
    print(bu2)
    return(bu2)

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("div.title-page p.info-title")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[0].replace("|","")
    bu1 = bu.split(" ")
    dd = bu1[2]
    mm = bu1[3]
    yy = bu1[4]

    months = ['ม.ค','ก.พ','มี.ค','เม.ย','พ.ค','มิ.ย','ก.ค','ส.ค','ก.ย','ต.ค','พ.ย','ธ.ค']
    for i in months:
        if i == mm:
            mm = str(months.index(i)+1)

    fulldate = (yy +'-'+ mm +'-'+dd)
    print(fulldate)
    return(fulldate)

def Main(links):
    Car_upload=[]
    c = database.cursor()
    for i in links:
        r = requests.get(i)
        soup = BeautifulSoup(r.text, "lxml")
        CarDetail = {}
        CarDetail['pri'] = get_Price(soup)
        CarDetail['mod'] = get_Model(soup)
        CarDetail['yea'] = get_Year(soup)
        CarDetail['col'] = get_Color(soup)
        CarDetail['mil'] = get_Mileage(soup)
        CarDetail['nam'] = get_SellName(soup)
        CarDetail['tel'] = get_SellTel(soup)
        CarDetail['loc'] = get_Location(soup)
        CarDetail['dat'] = get_Date(soup)
        Car_upload.append(CarDetail)
    if c:
        c.close()
    uploadDB(Car_upload)

#Main('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/chevrolet-colorado-year-2011/%E0%B8%82%E0%B8%B2%E0%B8%A2%E0%B8%A3%E0%B8%96-%E0%B8%97%E0%B8%B5%E0%B9%88-%E0%B8%8A%E0%B8%A5%E0%B8%9A%E0%B8%B8%E0%B8%A3%E0%B8%B5-aid7097521')
#Main('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/ford-fiesta-year-2012/2012-%E0%B8%AA%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B8%94%E0%B8%B5-aid7135721')
#Main('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/bmw-series-3-year-2017/%E0%B8%82%E0%B8%B2%E0%B8%A2%E0%B8%A3%E0%B8%96-%E0%B8%97%E0%B8%B5%E0%B9%88-%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A3-aid7224731')
#Main('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/bmw-x1-sdrive18i-year-2013/%E0%B8%82%E0%B8%B2%E0%B8%A2%E0%B8%A3%E0%B8%96-2013-%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%A7%E0%B8%A2%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%94%E0%B8%B5-aid7227941')
#Main('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/toyota-fortuner-year-2014/%E0%B8%82%E0%B8%B2%E0%B8%A2%E0%B8%A3%E0%B8%96-%E0%B8%97%E0%B8%B5%E0%B9%88-%E0%B8%AA%E0%B8%A1%E0%B8%B8%E0%B8%97%E0%B8%A3%E0%B8%9B%E0%B8%A3%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3-aid7302691')
#Main('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/mitsubishi--year-1995/%E0%B8%82%E0%B8%B2%E0%B8%A2%E0%B8%A3%E0%B8%96-%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%E0%B8%AD%E0%B8%B7%E0%B9%88%E0%B8%99%E0%B9%86-%E0%B8%97%E0%B8%B5%E0%B9%88-%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A3-aid7302341')
#Main('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/toyota-corolla-year-2014/2014-%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%94%E0%B8%B5-aid7272321')
#Main('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/isuzu-d-max-year-2004/2004-%E0%B8%AA%E0%B8%A0%E0%B8%B2%E0%B8%9E%E0%B8%94%E0%B8%B5-aid7274281')
#Main('https://rodmuesong.com/รถสำหรับขาย/mitsubishi-space-wagon-gt-year-2008/2008-รับประกันใช้ดี-aid7407051')
#Main('https://rodmuesong.com/รถสำหรับขาย/mitsubishi-g-wagon-year-2002/ขายรถ-ที่-พัทลุง-aid7438631')
