import requests
from bs4 import BeautifulSoup
from upload_data import uploadToSql as uploadDB
import connect
db = connect.conDB()
import datetime
def get_Price(soup): #ราคา
    detail = soup.select("div.car_characteristics div.price")
    j=0
    backup=[]
    for i in detail:
        backup = i.text.strip().split(' ')
        j=j+1
    bu = backup[0].replace(",","")
    print(bu)
    return(bu)

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("div.features_table")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        backup2=backup[0][3].split('\t')
        j=j+1
    bu = backup2[1].replace(" ","")
    bu1 = "รถ" + bu
    if(bu == "แวน"):
        bu1 = "รถตู้"
    elif(bu == "รถทั้งหมด"):
        bu1 = "-"
    print(bu1)

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
    detail = soup.select("div.features_table")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        backup2=backup[0][3].split('\t')
        j=j+1
    bu = backup2[2].replace(" ","")
    bu1 = bu.replace(",","")
    bu2 = (bu1.lower())
    print(bu2)
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
    detail = soup.select("div.features_table")
    j=0
    a=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        backup2=backup[0][3].split('\t')
    for i in backup2:
            j=j+1
    if(j==3):
        bu2 = "-"
    else:
        bu = backup2[3].replace(" ","")
        bu1 = bu.replace(",","")
        bu2 = (bu1.lower())
    print(bu2)
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
    detail = soup.select("div.features_table")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        backup2=backup[0][7].split('\t')
        j=j+1
        if(backup2[1]=="ปี:  "):
            bu = backup2[5].replace(" ","")
            bu1 = bu.replace(",","")
            bu2 = (bu1.lower())
        else:
            bu2="-"
    print(bu2)
    return(bu2)

def get_Color(soup): #สีรถ
    detail = soup.select("div.features_table")
    j=0
    k=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    for i in backup[0]:
        k+=1
        if(i == "\tสี:"):
            backup2=backup[0][k].split('\t')
            bu = backup2[0].replace(" ","")
    bu1 = "สี"+bu
    print(bu1)
    return(bu1)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.features_table")
    j=0
    k=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    for i in backup[0]:
        k+=1
        if(i == "เกียร์:"):
            backup2=backup[0][k].split('\t')
            bu = backup2[4].replace(" ","")
    if(bu == "ไม่ระบุเกียร์"):
        bu5 = "-"
    else:
        bu1 = bu.replace("ออโต้","")
        bu2 = bu1.replace("ธรรมดา","")
        bu3 = bu2.replace("/","")
        bu4 = bu3.replace(" ","")
        if(bu4 == "manual"):
            bu5 = "เกียร์ธรรมดา"
        elif(bu4 == "Automatic"):
            bu5 = "เกียร์อัตโนมัติ"
    print(bu5)
    return(bu5)

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div.features_table a")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[0].replace(" ","")
    if(bu == "ไม่ระบุเลขไมล์"):
        bu3 = "-"
    elif(bu == "ไม่เกิน 5,000 km"):
        bu3 = "4999"
    elif(bu == "มากกว่า 500,000 km"):
        bu3 = "500001"
    else:
        bu1 = bu.replace("km","")
        bu2 = bu1.replace(",","")
        bu3 = bu2
        #bu5 = bu4[0]+bu4[1]+bu4[2]+bu4[3]+bu4[4]
        #bu6 = bu4[5]+bu4[6]+bu4[7]+bu4[8]+bu4[9]
        #bu7 = (int(bu5)+int(bu6))/2
    print(bu3)
    return(bu3)

def get_SellName(soup): #ชื่อผู้ขาย
    detail = soup.select("span.name_author")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[0]
    print(bu)
    return(bu)

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("span.showphone a")
    j=0
    backup=[]
    for i in detail:
        backup.append(i)
        j=j+1
    #print(detail)
    #print(backup)
    #bu = str(backup)
    #if(bu[74] == "\\"):
    #    bu1 = bu[65]+bu[66]+bu[67]+bu[68]+bu[69]+bu[70]+bu[71]+bu[72]+bu[73]+""
    #else:
    #    bu1 = bu[65]+bu[66]+bu[67]+bu[68]+bu[69]+bu[70]+bu[71]+bu[72]+bu[73]+bu[74]
    #print(bu1)
    #return(bu1)

def get_Location(soup): #จังหวัด
    detail = soup.select("div.features_table a")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[1]
    print(bu)
    return(bu)

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("div.features_table")
    j=0
    k=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    for i in backup[0]:
        k+=1
        if(i == "อัพเดท:"):
            backup2=backup[0][k].split('\t')
            bu = backup2[4].split(" ")
    if(bu[2] == "วินาทีที่แล้ว" or bu[2] == "นาทีที่แล้ว" or bu[2] == "ชั่วโมงที่แล้ว" or bu[1] == "เมื่อวาน"):
        x = datetime.datetime.now()
        dd = (x.year+543)
        mm1 = (x.strftime("%m"))
        yy = (x.strftime("%d"))
    else:
        dd = bu[1]
        mm = bu[2]
        yy = bu[3].replace(",","")
        months = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
        for i in months:
               mm1 = str(months.index(i)+1)
    fulldate = (str(yy) +'-'+ str(mm1) +'-'+ str(dd))
    print(fulldate)
    return(fulldate)

def Main(links):
    Car_upload=[]
    for i in links:
        r = requests.get(i)
        soup = BeautifulSoup(r.text, "lxml")
        CarDetail = {}
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

#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/toyotacamry-138983.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/suzukiswift-143442.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/mitsubishi-143441.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/toyotahiace-143367.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/hondajazz-143307.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/isuzud-max-%E0%B8%9B%E0%B8%B512-15-143542.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/volvos80-147608.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/toyotacamry-144804.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/toyotahilux-vigo-144808.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/toyotacorolla-altis-147815.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/fordeverest-147686.html')

#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/toyotavellfire-139225.html')
