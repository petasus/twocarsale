import requests
from bs4 import BeautifulSoup
from upload_data import uploadToSql as uploadDB
import connect
import datetime
import time
db = connect.conDB()

def get_Price(soup): #ราคา
    detail = soup.select("div.price")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0]
    if(bu == "ติดต่อผู้ขาย"):
        pce = "0"
    else:
        bu1 = bu.replace(",","")
        pce = bu1.replace(" ","")
    print(pce)
    return(pce)

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("div.main-tab ul")
    backup=[]
    j=0
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        if(i == "ประเภทรถ"):
            bu = backup[0][j]
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
            elif(bu == "ยี่ห้อ"):
                tyc = '-'
            else:
                tyc = bu
            break
        else:
            tyc = "-"
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
    detail = soup.select("div.main-tab ul")
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    bu = (backup[0][1].lower())
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
    detail = soup.select("div.main-tab ul")
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    bu = (backup[0][3].lower())
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
    detail = soup.select("div.main-tab ul")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        j+=1
        if(i == "ปีที่ผลิต"):
            bu = backup[0][j]
            break
        else:
            bu = "-"
    print(bu)
    return(bu)

def get_Color(soup): #สีรถ
    detail = soup.select("div.main-tab ul")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        j+=1
        if(i == "สี"):
            bu = backup[0][j]
            break
        else:
            bu = "-"
    print(bu)
    return(bu)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.main-tab ul")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        j+=1
        if(i == "ระบบส่งกำลัง"):
            bu = backup[0][j]
            if(bu == "ระบบส่งกำลัง"):
                gr = "-"
                break
            else:
                gr = bu
                break
        else:
            gr = "-"
    print(gr)
    return(gr)

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div.main-tab ul")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        j+=1
        if(i == "เลขไมล"):
            bu = backup[0][j].replace("km","")
            bu1 = bu.replace(",","")
            mle = bu1.replace(" ","")
            break
        else:
            mle = "-"
    print(mle)
    return(mle)

def get_Seller(soup): #ชื่อผู้ขาย
    detail = soup.select("span.name-cat")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    if(backup == []):
        bu = "-"
    else:
        bu = backup[0]
    print(bu)
    return(bu)

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("span.span-hotline")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    if(backup == []):
        tlp = "-"
    else:
        bu = backup[0].replace(" ","")
        tlp = bu[0:10].replace(",","")
    print(tlp)
    return(tlp)

def get_Location(soup): #จังหวัด
    detail = soup.select("div.date")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split(' '))
    for i in backup[0]:
        j+=1
        if(j == 4):
            bu = backup[0][3]
            break
        else:
            bu = "-"
    print(bu)
    return bu

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("div.date")
    backup=[]
    months = ['ม.ค','ก.พ','มี.ค','เม.ย','พ.ค','มิ.ย','ก.ค','ส.ค','ก.ย','ต.ค','พ.ย','ธ.ค']
    for i in detail:
        backup.append(i.text.strip().split(' '))
    dd = backup[0][0]
    mm = backup[0][1]
    yy = backup[0][2].replace(",","")
    for i in months:
        if i == mm:
            mm = str(months.index(i)+1)
            if(int(mm) <= 9 ):
                mm = "0"+ str(mm)
    if(int(dd) <= 9 ):
        dd = "0"+ str(dd)
    day = (yy +'-'+ mm +'-'+dd)
    print(day)
    return(day)

def get_Image(soup):
    detail = soup.select("div.thumb img.cursor-p")
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

def get_ErrorCheck(soup):
    detail = soup.select("div.ta-center h1")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    if(backup == []):
        bu = 1
    else:
        bu = 0
    print(bu)
    return(bu)

def get_CheckUpdate(soup):
    detail = soup.select("div.date")
    months = ['ม.ค','ก.พ','มี.ค','เม.ย','พ.ค','มิ.ย','ก.ค','ส.ค','ก.ย','ต.ค','พ.ย','ธ.ค']
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split(' '))
    print(backup)
    if(backup == []):
        chu = 0
    else:
        dd = backup[0][0]
        mm = backup[0][1]
        yy = backup[0][2].replace(",","")
        yy = int(yy)-2543
        for i in months:
            if i == mm:
                mm = str(months.index(i)+1)
                if(int(mm) <= 9 ):
                    mm = "0"+ str(mm)
        if(int(dd) <= 9 ):
            dd = "0"+ str(dd)
        day = str(mm)+"/"+str(dd)+"/"+str(yy)
        xx = datetime.datetime.now()
        xd = xx.strftime("%x")
        if(day == xd):
            print("0")
            chu = 0
        else:
            chu = 1
    print(chu)
    return(chu)

def get_Reserved(soup): #ซื้อขายแล้ว
    detail = soup.select("div.box-sold p")
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
        j+=1
        soup = BeautifulSoup(r.text, "lxml")
        CarDetail = {}
        CarDetail['err'] = get_ErrorCheck(soup)
        if(CarDetail['err']== 0):
            continue
        CarDetail['che'] = get_CheckUpdate(soup)
        if(CarDetail['che']== 0):
            continue
        CarDetail['res'] = get_Reserved(soup)
        if(CarDetail['res']== 0):
            continue
        CarDetail['pri'] = get_Price(soup)
        CarDetail['mod'] = get_Model(soup)
        CarDetail['yea'] = get_Year(soup)
        CarDetail['col'] = get_Color(soup)
        CarDetail['mil'] = get_Mileage(soup)
        CarDetail['nam'] = get_Seller(soup)
        CarDetail['tel'] = get_SellTel(soup)
        CarDetail['loc'] = get_Location(soup)
        CarDetail['dat'] = get_Date(soup)
        CarDetail['img'] = get_Image(soup)
        Car_upload.append(CarDetail)
    uploadDB(Car_upload)

#link='https://unseencar.com/taladrod/suzuki-ciaz-year-2016/1-2-rs-โฉมปี-15-17-aid245152'
#r = requests.get(link)
#soup = BeautifulSoup(r.text, "lxml")
#get_ErrorCheck(soup)
#get_CheckUpdate(soup)
#get_Reserved(soup)
#get_Image(soup)
