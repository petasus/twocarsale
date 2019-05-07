import requests
from bs4 import BeautifulSoup
from upload_data import uploadToSql as uploadDB
import connect
db = connect.conDB()
import datetime
def get_Price(soup): #ราคา
    detail = soup.select("h1.red")
    backup=[]
    for i in detail:
        backup = i.text.strip().split(' ')
    bu = backup[2]
    bu1 = bu.replace(",","")
    print(bu1)
    return(bu1)

def get_TypeCar(soup): #ประเภทรถ
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
    bu = backup[2]
    bu1 = (bu.lower())
    print(bu1)
    while(True):
        CKsql = """ SELECT id FROM brand WHERE `name`=%s"""
        c = db.cursor()
        CKExis = c.execute(CKsql,(bu1))
        if CKExis:
            getID = c.fetchall()
            return getID[0][0]
        else:
            c.execute("""INSERT INTO brand (`name`) VALUES (%s)""", (bu1))
            db.commit()
            continue

def get_Model(soup): #รุ่น
    detail = soup.select("table.table td")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[5]
    bu1 = (bu.lower())
    print(bu1)
    TypeCar = get_TypeCar(soup)
    Brand = get_Brand(soup)
    Gear = get_Gear(soup)
    while(True):
        CKsql = """ SELECT id FROM model WHERE `name`=%s AND `bnd_id`=%s AND `typ_id`=%s"""
        c = db.cursor()
        CKExis = c.execute(CKsql,(bu1,Brand,TypeCar))
        if CKExis:
            getID = c.fetchall()
            return getID[0][0]
        else:
            c.execute("""INSERT INTO model (`name`,`bnd_id`,`typ_id`,`gears`) VALUES (%s,%s,%s,%s)""", (bu1,Brand,TypeCar,Gear))
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
    bu = backup[23]
    bu1 = "สี"+bu
    print(bu1)
    return(bu1)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("table.table td")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[32]
    if(bu == "Manual"):
        bu1 = "เกียร์ธรรมดา"
    elif(bu == "Automatic"):
        bu1 = "เกียร์อัตโนมัติ"
    print(bu1)
    return(bu1)

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("table.table td")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[26]
    bu1 = bu.replace("km","")
    bu2 = bu1.replace(" ","")
    print(bu2)
    return(bu2)

def get_SellName(soup): #ชื่อผู้ขาย
    detail = soup.select("div.name_profile a")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0]
    print(bu)
    return(bu)

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("div.name_profile ")
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    bu = backup[0][2].replace(" ","")
    print(bu)
    return(bu)

def get_Location(soup): #จังหวัด
    detail = soup.select("table.table td")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[17]
    print(bu)
    return(bu)

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("table.table td")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[50]
    bu1 = bu.split(" ")
    dd = bu1[0]
    mm = bu1[1]
    yy = (int(bu1[2])+2500)
    yy = str(yy)
    months = ['ม.ค.','ก.พ.','มี.ค.','เม.ย.','พ.ค.','มิ.ย.','ก.ค.','ส.ค.','ก.ย.','ต.ค.','พ.ย.','ธ.ค.']
    for i in months:
        if i == mm:
            mm = str(months.index(i)+1)
            if(int(mm) <= 9 ):
                mm = "0"+ str(mm)
    if(int(dd) <= 9 ):
        dd = "0"+ str(dd)
    fulldate = (yy +'-'+ mm +'-'+ dd)
    print(fulldate)
    return(fulldate)

def get_CheckUpdate(soup):
    detail = soup.select("table.table td")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[50]
    bu1 = bu.split(" ")
    dd = bu1[0]
    mm = bu1[1]
    yy = (int(bu1[2])+2500)
    yy = str(yy)
    months = ['ม.ค.','ก.พ.','มี.ค.','เม.ย.','พ.ค.','มิ.ย.','ก.ค.','ส.ค.','ก.ย.','ต.ค.','พ.ย.','ธ.ค.']
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

def get_Reserved(soup): #จองแล้ว
    detail = soup.select("div.name_profile ")
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    bu = backup[0][2].replace(" ","")
    if(bu=="จองแล้ว"):
        bu1 = 0
        print(bu1)
    else:
        bu1 = 1
        print(bu1)
    return(bu1)

def Main(links):
    Car_upload=[]
    for i in links:
        print(i)
        r = requests.get(i)
        soup = BeautifulSoup(r.text, "lxml")
        CarDetail = {}
        CarDetail['che'] = get_CheckUpdate(soup)
        if(CarDetail['che']== 0):
            continue
        CarDetail['res'] = get_Reserved(soup)
        if(CarDetail['res']== 0):
            continue
        CarDetail['pri'] = get_Price(soup)
        CarDetail['typ'] = get_TypeCar(soup)
        CarDetail['bnd'] = get_Brand(soup)
        CarDetail['mod'] = get_Model(soup)
        CarDetail['yea'] = get_Year(soup)
        CarDetail['col'] = get_Color(soup)
        CarDetail['gea'] = get_Gear(soup)
        CarDetail['mil'] = get_Mileage(soup)
        CarDetail['sel'] = get_SellName(soup)
        CarDetail['tel'] = get_SellTel(soup)
        CarDetail['loc'] = get_Location(soup)
        CarDetail['dat'] = get_Date(soup)
        Car_upload.append(CarDetail)
    uploadDB(Car_upload)

def Testl(links):
    for i in links:
        print(i)
        r = requests.get(i)
        soup = BeautifulSoup(r.text, "lxml")
        CarDetail = {}
        CarDetail['che'] = get_CheckUpdate(soup)
        if(CarDetail['che']== 0):
            continue
        CarDetail['res'] = get_Reserved(soup)
        if(CarDetail['res']== 0):
            continue
        CarDetail['pri'] = get_Price(soup)
        CarDetail['typ'] = get_TypeCar(soup)
        CarDetail['bnd'] = get_Brand(soup)
        CarDetail['mod'] = get_Model(soup)
        CarDetail['yea'] = get_Year(soup)
        CarDetail['col'] = get_Color(soup)
        CarDetail['gea'] = get_Gear(soup)
        CarDetail['mil'] = get_Mileage(soup)
        CarDetail['sel'] = get_SellName(soup)
        CarDetail['tel'] = get_SellTel(soup)
        CarDetail['loc'] = get_Location(soup)
        CarDetail['dat'] = get_Date(soup)

def Test(links):
    print(links)
    r = requests.get(links)
    soup = BeautifulSoup(r.text, "lxml")
    CarDetail = {}
    CarDetail['che'] = get_CheckUpdate(soup)
    CarDetail['res'] = get_Reserved(soup)
    CarDetail['pri'] = get_Price(soup)
    CarDetail['typ'] = get_TypeCar(soup)
    CarDetail['bnd'] = get_Brand(soup)
    CarDetail['mod'] = get_Model(soup)
    CarDetail['yea'] = get_Year(soup)
    CarDetail['col'] = get_Color(soup)
    CarDetail['gea'] = get_Gear(soup)
    CarDetail['mil'] = get_Mileage(soup)
    CarDetail['sel'] = get_SellName(soup)
    CarDetail['tel'] = get_SellTel(soup)
    CarDetail['loc'] = get_Location(soup)
    CarDetail['dat'] = get_Date(soup)

#Test('https://www.traderod.com/cars/view.php?id_car=66634')
#Test('https://www.traderod.com/cars/view.php?id_car=66606')
#Test('https://www.traderod.com/cars/view.php?id_car=66054')
#Main('')
#Main('')
#Main('')
