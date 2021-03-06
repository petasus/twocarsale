import requests
from bs4 import BeautifulSoup
from upload_data import uploadToSql as uploadDB
import connect
db = connect.conDB()
import datetime
import time
def get_Price(soup): #ราคา
    detail = soup.select("div.car_characteristics div.price")
    backup=[]
    for i in detail:
        backup = i.text.strip().split(' ')
    bu = backup[0].replace(",","")
    print(bu)
    return(bu)

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("div.features_table")
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        backup2=backup[0][3].split('\t')
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
        CKExis = c.execute(CKsql,(bu1))
        if CKExis:
            getID = c.fetchall()
            return getID[0][0]
        else:
            c.execute("""INSERT INTO type_car (`name`) VALUES (%s)""", (bu1))
            db.commit()
            continue

def get_Brand(soup): #ยี่ห้อ
    detail = soup.select("div.features_table")
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        backup2=backup[0][3].split('\t')
    bu = backup2[2].replace(" ","")
    bu1 = bu.replace(",","")
    bu2 = (bu1.lower())
    print(bu2)
    while(True):
        CKsql = """ SELECT id FROM brand WHERE `name`=%s"""
        c = db.cursor()
        CKExis = c.execute(CKsql,(bu2))
        if CKExis:
            getID = c.fetchall()
            return getID[0][0]
        else:
            c.execute("""INSERT INTO brand (`name`) VALUES (%s)""", (bu2))
            db.commit()
            continue

def get_Model(soup): #รุ่น
    detail = soup.select("div.features_table")
    j=0
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
        CKExis = c.execute(CKsql,(bu2,Brand,TypeCar))
        if CKExis:
            getID = c.fetchall()
            return getID[0][0]
        else:
            c.execute("""INSERT INTO model (`name`,`bnd_id`,`typ_id`,`gears`) VALUES (%s,%s,%s,%s)""", (bu2,Brand,TypeCar,Gear))
            db.commit()
            continue

def get_Year(soup): #รุ่นปี
    detail = soup.select("div.features_table")
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        backup2=backup[0][7].split('\t')
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
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        j+=1
        if(i == "\tสี:"):
            backup2=backup[0][j].split('\t')
            bu = backup2[0].replace(" ","")
    bu1 = "สี"+bu
    print(bu1)
    return(bu1)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.features_table")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        j+=1
        if(i == "เกียร์:"):
            backup2=backup[0][j].split('\t')
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
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
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

def get_Seller(soup): #ชื่อผู้ขาย
    detail = soup.select("span.name_author")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    if(backup[0]==''):
        bu = '-'
    else:
        bu = backup[0]
    print(bu)
    return(bu)

def get_SellTel(soup): #เบอร์ผู้ขาย #onclick
    detail = soup.select("span.showphone a")
    bu="-"
    print(bu)
    return(bu)
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
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    if(backup[1]==''):
        bu = '-'
    else:
        bu = backup[1]
    print(bu)
    return(bu)

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("div.features_table")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        j+=1
        if(i == "อัพเดท:"):
            backup2=backup[0][j].split('\t')
            bu = backup2[4].split(" ")
    if(bu[2] == "วินาทีที่แล้ว" or bu[2] == "นาทีที่แล้ว" or bu[2] == "ชั่วโมงที่แล้ว" or bu[1] == "เมื่อวาน"):
        x = datetime.datetime.now()
        dd = (x.year+543)
        mm = (x.strftime("%m"))
        yy = (x.strftime("%d"))
    else:
        dd = bu[1]
        mm = bu[2]
        yy = bu[3].replace(",","")
        months = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
        for i in months:
            mm = str(months.index(i)+1)
            if(int(mm) <= 9 ):
                mm = "0"+ str(mm)
    if(int(dd) <= 9 ):
        dd = "0"+ str(dd)
    fulldate = (str(yy) +'-'+ str(mm) +'-'+ str(dd))
    print(fulldate)
    return(fulldate)

def get_Image(soup):
    detail = soup.select("div.fotorama img")
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
            pic += 'https://xn--22caobb7fvah1fc9id1dce1ti4me.net'+backup[k]+" "
            k+=1
    print(pic)
    return(pic)

def get_CheckUpdate(soup):
    detail = soup.select("div.features_table")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    if(backup == []):
        bu = 0
    else:
        for i in backup[0]:
            j+=1
            if(i == "อัพเดท:"):
                backup2=backup[0][j].split('\t')
                bu = backup2[4].split(" ")
        if(bu[2] == "วินาทีที่แล้ว" or bu[2] == "นาทีที่แล้ว" or bu[2] == "ชั่วโมงที่แล้ว" or bu[1] == "เมื่อวาน"):
            x = datetime.datetime.now()
            yy = (x.year+543)
            mm = (x.strftime("%m"))
            dd = (x.strftime("%d"))
        else:
            dd = bu[1]
            mm = bu[2]
            yy = bu[3].replace(",","")
            months = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
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
            bu = 0
        else:
            bu = 1
    print(bu)
    return(bu)

def get_ErrorCheck(soup):
    detail = soup.select("div.catalog_desc div.title_box h4")
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
        soup = BeautifulSoup(r.text,"lxml")
        CarDetail = {}
        CarDetail['err'] = get_ErrorCheck(soup)
        if(CarDetail['err']== 0):
            continue
        CarDetail['che'] = get_CheckUpdate(soup)
        if(CarDetail['che']== 0):
            continue
        CarDetail['pri'] = get_Price(soup)
        CarDetail['typ'] = get_TypeCar(soup)#
        CarDetail['bnd'] = get_Brand(soup)#
        CarDetail['mod'] = get_Model(soup)
        CarDetail['yea'] = get_Year(soup)
        CarDetail['col'] = get_Color(soup)
        CarDetail['gea'] = get_Gear(soup)#
        CarDetail['mil'] = get_Mileage(soup)
        CarDetail['nam'] = get_Seller(soup)
        CarDetail['tel'] = get_SellTel(soup)
        CarDetail['loc'] = get_Location(soup)
        CarDetail['dat'] = get_Date(soup)
        CarDetail['img'] = get_Image(soup)
        Car_upload.append(CarDetail)
    uploadDB(Car_upload)

#link='https://xn--22caobb7fvah1fc9id1dce1ti4me.net/nissanalmera-98059.html'
#r = requests.get(link)
#soup = BeautifulSoup(r.text,"lxml")
#get_Image(soup)
#get_Location(soup)
