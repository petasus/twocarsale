import requests
from bs4 import BeautifulSoup
from upload_data import uploadToSql as uploadDB
import connect
import datetime
import time
db = connect.conDB()

def get_Price(soup): #ราคา
    detail = soup.select("div.left-content p.price")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0]
    if(bu == "ติดต่อผู้ขาย"):
        pce = "0"
    else:
        bu1 = bu.replace("บาท","")
        bu2 = bu1.replace(",","")
        pce = bu2.replace(" ","")
    print(pce)
    return(pce)

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "ประเภทรถ" ):
            k = j+1
        j=j+1
    if(k != 1000):
        bu = (backup[k].lower())
    else:
        bu = "-"
    if(bu == "รถเก๋ง 4 ประตู" or bu == "รถเก๋ง 5 ประตู"):
        tyc = "รถเก๋ง"
    elif(bu == "SUV" or bu == "suv"):
        tyc = "รถSUV"
    elif(bu == "Truck" or bu == "truck"):
        tyc = "รถบรรทุก"
    elif(bu == "Wagon" or bu == "wagon"):
        tyc = "รถWagon"
    elif(bu == "รถตู้/MPV" or bu == "รถตู้/mpv" or bu == "รถตู้/VAN" or bu == "รถตู้/van"):
        tyc = "รถตู้"
    elif(bu == "รถเก๋ง 2 ประตู" or bu == "รถเปิดประทุน" or bu == "Cabriolet" or bu == "cabriolet"):
        tyc = "รถสปอร์ต"
    else:
        tyc = bu
    print(tyc)
    while(True):
        CKsql = """ SELECT id FROM type_car WHERE `name`=%s"""
        c = db.cursor()
        CKExis = c.execute(CKsql,(tyc))
        if CKExis:
            getID = c.fetchall()
            return getID[0][0]
        else:
            c.execute("""INSERT INTO type_car (`name`) VALUES (%s)""", (tyc))
            db.commit()
            continue

def get_Brand(soup): #ยี่ห้อ
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "ยี่ห้อ" ):
            k = j+1
        j=j+1
    if(k != j):
        bu = (backup[k].lower())
    else:
        bu = "-"
    print(bu)
    while(True):
        CKsql = """ SELECT id FROM brand WHERE `name`=%s"""
        c = db.cursor()
        CKExis = c.execute(CKsql,(bu))
        if CKExis:
            getID = c.fetchall()
            return getID[0][0]
        else:
            c.execute("""INSERT INTO brand (`name`) VALUES (%s)""", (bu))
            db.commit()
            continue

def get_Model(soup): #รุ่น
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "รุ่น" ):
            k = j+1
        j=j+1
    if(k != 1000):
        bu = (backup[k].lower())
    else:
        bu = "-"
    print(bu)
    TypeCar = get_TypeCar(soup)
    Brand = get_Brand(soup)
    Gear = get_Gear(soup)
    while(True):
        CKsql = """ SELECT id FROM model WHERE `name`=%s AND `bnd_id`=%s AND `typ_id`=%s"""
        c = db.cursor()
        CKExis = c.execute(CKsql,(bu,Brand,TypeCar))
        if CKExis:
            getID = c.fetchall()
            return getID[0][0]
        else:
            c.execute("""INSERT INTO model (`name`,`bnd_id`,`typ_id`,`gears`) VALUES (%s,%s,%s,%s)""", (bu,Brand,TypeCar,Gear))
            db.commit()
            continue

def get_Year(soup): #รุ่นปี
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "ปีที่ผลิต" ):
            k = j+1
        j=j+1
    if(k != 1000):
        bu = backup[k]
    else:
        bu = "-"
    print(bu)
    return(bu)

def get_Color(soup): #สีรถ
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "สี" ):
            k = j+1
        j=j+1
    if(k != 1000):
        bu = backup[k]
    else:
        bu = "-"
    print(bu)
    return(bu)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "ระบบส่งกำลัง" ):
            k = j+1
        j=j+1
    if(k != 1000):
        bu = backup[k]
    else:
        bu = "-"
    print(bu)
    return(bu)

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "เลขไมล์" ):
            k = j+1
        j=j+1
    if(k != 1000):
        bu = backup[k].replace(",","")
    else:
        bu = "-"
    print(bu)
    return(bu)

def get_SellName(soup): #ชื่อผู้ขาย
    detail = soup.select("div.col-box h4")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0]
    if(bu == ''):
        sname = "-"
    else:
        sname = bu
    print(sname)
    return(sname)

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("div.col-box span")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0].replace(".","")
    print(bu)
    return(bu)

def get_Location(soup): #จังหวัด
    detail = soup.select("div.title-page p.info-title")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0].split(" ")
    lct = bu[0]
    print(lct)
    return(lct)

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("div.title-page p.info-title")
    backup=[]
    months = ['ม.ค','ก.พ','มี.ค','เม.ย','พ.ค','มิ.ย','ก.ค','ส.ค','ก.ย','ต.ค','พ.ย','ธ.ค']
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0].split(" ")
    dd = bu[2]
    mm = bu[3]
    yy = bu[4]
    for i in months:
        if i == mm:
            mm = str(months.index(i)+1)
            if(int(mm) <= 9 ):
                mm = "0"+str(mm)
    if(int(dd) <= 9 ):
        dd = "0"+str(dd)
    day = (yy +'-'+ mm +'-'+dd)
    print(day)
    return(day)

def get_Image(soup):
    detail = soup.select("a.imageGallery img")
    j=0
    k=0
    pic=""
    backup=[]
    for i in detail:
        backup.append(i['src'])
        j+=1
    if(j==0):
        pic="-"
    else:
        while(k != j):
            pic += backup[k]+" "
            k+=1
    print(pic)
    return(pic)

def get_CheckUpdate(soup):
    detail = soup.select("div.title-page p.info-title")
    backup=[]
    months = ['ม.ค','ก.พ','มี.ค','เม.ย','พ.ค','มิ.ย','ก.ค','ส.ค','ก.ย','ต.ค','พ.ย','ธ.ค']
    for i in detail:
        backup.append(i.text.strip())
    print(backup)
    if(backup == []):
        chd = 0
    else:
        bu = backup[0].split(" ")
        dd = bu[2]
        mm = bu[3]
        yy = bu[4]
        yy = int(yy)-2543
        for i in months:
            if(i == mm):
                mm = str(months.index(i)+1)
                if(int(mm) <= 9 ):
                    mm = "0"+str(mm)
        if(int(dd) <= 9 ):
            dd = "0"+str(dd)
        day = str(mm)+"/"+str(dd)+"/"+str(yy)
        xx = datetime.datetime.now()
        xd = xx.strftime("%x")
        if(day == xd):
            chd = 0
        else:
            chd = 1
    print(chd)
    return(chd)

def get_ErrorCheck(soup):
    detail = soup.select("div.title h4.fweight-bold")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    if(backup == []):
        bu = 1
    else:
        bu = 0
    print(bu)
    return(bu)

def Main(links):
    Car_upload=[]
    j=1
    for i in links:
        print("link no." + str(j) + " " + i)
        while True:
            try:
                r = requests.get(i)
                break
            except:
                print("มีปัญหากลับไปรีเควสใหม่")
                print("ที่ลิ้ง: "+str(i))
                time.sleep(10)
                continue
        soup = BeautifulSoup(r.text, "lxml")
        j+=1
        CarDetail = {}
        CarDetail['err'] = get_ErrorCheck(soup)
        if(CarDetail['err']== 0):
            continue
        CarDetail['che'] = get_CheckUpdate(soup)
        if(CarDetail['che']== 0):
            continue
        CarDetail['pri'] = get_Price(soup)
        CarDetail['mod'] = get_Model(soup)
        CarDetail['yea'] = get_Year(soup)
        CarDetail['col'] = get_Color(soup)
        CarDetail['mil'] = get_Mileage(soup)
        CarDetail['nam'] = get_SellName(soup)
        CarDetail['tel'] = get_SellTel(soup)
        CarDetail['loc'] = get_Location(soup)
        CarDetail['dat'] = get_Date(soup)
        CarDetail['img'] = get_Image(soup)
        Car_upload.append(CarDetail)
    uploadDB(Car_upload)

#link='https://rodmuesong.com/รถสำหรับขาย/nissan-march-year-2013/2013-สภาพดี-aid7533811'
#link='https://rodmuesong.com/รถสำหรับขาย/toyota-hilux-vigo-year-2005/2005-สภาพดี-aid7531091'
#link='https://rodmuesong.com/รถสำหรับขาย/chrysler-neon-year-1996/1996-สภาพดี-aid7223411'
#link='https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/ford-ecosport-trend-year-2014/2014-1-5-at-aid7581343'
#r = requests.get(link)
#soup = BeautifulSoup(r.text, "lxml")
#get_CheckUpdate(soup)
#get_Price(soup)
#get_Model(soup)
#get_Year(soup)
#get_Color(soup)
#get_Mileage(soup)
#get_SellName(soup)
#get_SellTel(soup)
#get_Location(soup)
#get_Date(soup)
#get_Image(soup)
