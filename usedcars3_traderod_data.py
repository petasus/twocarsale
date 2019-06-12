import requests
from bs4 import BeautifulSoup
from upload_data import uploadToSql as uploadDB
import connect
import datetime
import time
db = connect.conDB()

def get_Price(soup): #ราคา
    detail = soup.select("h1.red")
    backup=[]
    for i in detail:
        backup = i.text.strip().split(' ')
    bu = backup[2].replace(",","")
    print(bu)
    return(bu)

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("table.table td")
    bu = "-"
    print(bu)
    while(True):
        CKsql = """ SELECT id FROM type_car WHERE `name`=%s"""
        c = db.cursor()
        CKExis = c.execute(CKsql,(bu))
        if CKExis:
            getID = c.fetchall()
            return getID[0][0]
        else:
            c.execute("""INSERT INTO type_car (`name`) VALUES (%s)""", (bu))
            db.commit()
            continue

def get_Brand(soup): #ยี่ห้อ
    detail = soup.select("table.table td")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = (backup[2].lower())
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
    detail = soup.select("table.table td")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = (backup[5].lower())
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
    detail = soup.select("table.table td")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[14]
    print(bu)
    return(bu)

def get_Color(soup): #สีรถ
    detail = soup.select("table.table td")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = "สี"+backup[23]
    print(bu)
    return(bu)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("table.table td")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[32]
    if(bu == "Manual"):
        gr = "เกียร์ธรรมดา"
    elif(bu == "Automatic"):
        gr = "เกียร์อัตโนมัติ"
    print(gr)
    return(gr)

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("table.table td")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[26].replace("km","")
    mle = bu.replace(" ","")
    print(mle)
    return(mle)

def get_Seller(soup): #ชื่อผู้ขาย
    detail = soup.select("div.name_profile a")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0]
    print(bu)
    return(bu)

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("div.name_profile a")
    backup=[]
    j=0
    for i in detail:
        backup.append(i.text.strip())
        j+=1
    print(backup)
    if(j<=1):
        bu = "-"
    else:
        bu = backup[1]
    print(bu)
    return(bu)

def get_Location(soup): #จังหวัด
    detail = soup.select("table.table td")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    if(backup[17]== ''):
        bu = "-"
    else:
        bu = backup[17]
    print(bu)
    return(bu)

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("table.table td")
    backup=[]
    months = ['ม.ค.','ก.พ.','มี.ค.','เม.ย.','พ.ค.','มิ.ย.','ก.ค.','ส.ค.','ก.ย.','ต.ค.','พ.ย.','ธ.ค.']
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[50].split(" ")
    dd = bu[0]
    mm = bu[1]
    yy = str(int(bu[2])+2500)
    for i in months:
        if i == mm:
            mm = str(months.index(i)+1)
            if(int(mm) <= 9 ):
                mm = "0"+ str(mm)
    if(int(dd) <= 9 ):
        dd = "0"+ str(dd)
    day = (yy +'-'+ mm +'-'+ dd)
    print(day)
    return(day)

def get_Image(soup):
    detail = soup.select("a.fancybox img")
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
    detail = soup.select("table.table td")
    backup=[]
    months = ['ม.ค.','ก.พ.','มี.ค.','เม.ย.','พ.ค.','มิ.ย.','ก.ค.','ส.ค.','ก.ย.','ต.ค.','พ.ย.','ธ.ค.']
    for i in detail:
        backup.append(i.text.strip())
    print(backup)
    if(backup == []):
        chu = 0
    else:
        bu = backup[50].split(" ")
        dd = bu[0]
        mm = bu[1]
        yy = (int(bu[2])-43)
        xx = datetime.datetime.now()
        xd = xx.strftime("%x")
        for i in months:
            if i == mm:
                mm = str(months.index(i)+1)
                if(int(mm) <= 9 ):
                    mm = "0"+ str(mm)
        if(int(dd) <= 9 ):
            dd = "0"+ str(dd)
        day = str(mm)+"/"+str(dd)+"/"+str(yy)
        if(day == xd):
            chu = 0
        else:
            chu = 1
    print(chu)
    return(chu)

def get_Reserved(soup): #จองแล้ว
    detail = soup.select("div.")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    print(backup)
    if(backup == ['']):
        rse = 1
    else:
        rse = 0
    print(rse)
    return(rse)

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

#link='https://www.traderod.com/cars/view.php?id_car=65678'
#link='https://www.traderod.com/cars/view.php?id_car=58104'#สี
#r = requests.get(link)
#soup = BeautifulSoup(r.text,"lxml")
#get_Location(soup)
