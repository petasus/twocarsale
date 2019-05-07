import requests
from bs4 import BeautifulSoup
from upload_data import uploadToSql as uploadDB
import connect
import datetime
db = connect.conDB()

def get_Price(soup): #ราคา
    detail = soup.select("div.left-content p.price")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu0 = backup[0]
    if(bu0 == "ติดต่อผู้ขาย"):
        bu3 = "0"
    else:
        bu = bu0
        bu1 = bu.replace("บาท","")
        bu2 = bu1.replace(",","")
        bu3 = bu2.replace(" ","")
    print(bu3)
    return(bu3)

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("div.content-col div.item-row span")
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
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
    elif(bu == "รถเก๋ง 2 ประตู" or bu == "รถเปิดประทุน" or bu == "Cabriolet" or bu == "cabriolet"):
        bu1 = "รถสปอร์ต"
    else:
        bu1 = bu
    print(bu1)
    while(True):
        CKsql = """ SELECT id FROM type_car WHERE `name`=%s"""
        c = db.cursor()
        CKExis = c.execute(CKsql,(bu1))
        if CKExis:
            getID = c.fetchall()
            return getID[0][0]
        else:
            c.execute("""INSERT INTO type_car (`name`) VALUES (%s)""", (bu1))
            db.commit()
            continue

def get_Brand(soup): #ยี่ห้อ
    detail = soup.select("div.content-col div.item-row span")
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
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
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
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
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
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
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
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
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
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
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
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
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0]
    if(bu == ''):
        bu1 = "-"
    else:
        bu1 = bu
    print(bu1)
    return(bu1)

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
    bu = backup[0].replace("|","")
    bu1 = bu.split(" ")
    bu2 = bu1[0]
    print(bu2)
    return(bu2)

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("div.title-page p.info-title")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0].replace("|","")
    bu1 = bu.split(" ")
    dd = bu1[2]
    mm = bu1[3]
    yy = bu1[4]
    months = ['ม.ค','ก.พ','มี.ค','เม.ย','พ.ค','มิ.ย','ก.ค','ส.ค','ก.ย','ต.ค','พ.ย','ธ.ค']
    for i in months:
        if i == mm:
            mm = str(months.index(i)+1)
            if(int(mm) <= 9 ):
                mm = "0"+ str(mm)
    if(int(dd) <= 9 ):
        dd = "0"+ str(dd)
    fulldate = (yy +'-'+ mm +'-'+dd)
    print(fulldate)
    return(fulldate)

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
    for i in detail:
        backup.append(i.text.strip())
    print(backup)
    bu = backup[0].split(" ")
    print(bu)
    dd = bu[2]
    mm = bu[3]
    yy = bu[4]
    months = ['ม.ค','ก.พ','มี.ค','เม.ย','พ.ค','มิ.ย','ก.ค','ส.ค','ก.ย','ต.ค','พ.ย','ธ.ค']
    for i in months:
        if i == mm:
            mm = str(months.index(i)+1)
            if(int(mm) <= 9 ):
                mm = "0"+ str(mm)
    if(int(dd) <= 9 ):
        dd = "0"+ str(dd)
    yy = int(yy)-2543
    day = str(mm)+"/"+str(dd)+"/"+str(yy)
    xx = datetime.datetime.now()
    x = xx.strftime("%x")
    if(day == x):
        print("0")
        bu = 0
    else:
        print("1")
        bu = 1
    return(bu)

def get_ErrorCheck(soup):
    detail = soup.select("div.title h4.fweight-bold")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    if(backup == []):
        print("1")
        bu = 1
    else:
        print("0")
        bu = 0
    return(bu)

def Main(links):
    Car_upload=[]
    j=1
    for i in links:
        print("link no." + str(j) + " " + i)
        r = requests.get(i)
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
