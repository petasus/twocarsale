import requests
from bs4 import BeautifulSoup

def get_Price(soup): #ราคา
    detail = soup.select("div.price")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[0]
    if(bu == "ติดต่อผู้ขาย"):
        bu3 = "-"
    else:
        bu1 = bu
        bu2 = bu1.replace(",","")
        bu3 = bu2.replace(" ","")
    print(bu3)
    return(bu)

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("div.main-tab ul")
    j=0
    k=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    for i in backup[0]:
        k+=1
        if(i == "ประเภทรถ"):
            bu = backup[0][k]
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
            break
        else:
            bu1 = "-"
    print(bu1)
    return(bu1)

def get_Brand(soup): #ยี่ห้อ
    detail = soup.select("div.main-tab ul")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    #print(backup)
    bu = backup[0][1]
    bu1 = (bu.lower())
    print(bu1)
    return(bu1)

def get_Model(soup): #รุ่น
    detail = soup.select("div.main-tab ul")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    #print(backup)
    bu = backup[0][3]
    bu1 = (bu.lower())
    print(bu1)
    return(bu1)

def get_Year(soup): #รุ่นปี
    detail = soup.select("div.main-tab ul")
    j=0
    k=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    for i in backup[0]:
        k+=1
        if(i == "ปีที่ผลิต"):
            bu = backup[0][k]
            break
        else:
            bu = "-"
    print(bu)
    return(bu)

def get_Color(soup): #สีรถ
    detail = soup.select("div.main-tab ul")
    j=0
    k=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    for i in backup[0]:
        k+=1
        if(i == "สี"):
            bu = backup[0][k]
            break
        else:
            bu = "-"
    print(bu)
    return(bu)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.main-tab ul")
    j=0
    k=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    for i in backup[0]:
        k+=1
        if(i == "ระบบส่งกำลัง"):
            bu = backup[0][k]
            if(bu == "ระบบส่งกำลัง"):
                bu1 = "-"
            break
        else:
            bu1 = "-"
    print(bu1)
    return(bu1)

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div.main-tab ul")
    j=0
    k=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    for i in backup[0]:
        k+=1
        if(i == "เลขไมล"):
            bu = backup[0][k]
            bu1 = bu.replace("km","")
            bu2 = bu1.replace(",","")
            bu3 = bu2.replace(" ","")
            break
        else:
            bu3 = "-"
    print(bu3)
    return(bu3)

def get_Seller(soup): #ชื่อผู้ขาย
    #detail = soup.select("div.info-c div.short-c")
    detail = soup.select("span.name-cat")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    if(backup == []):
        bu = "-"
    else:
        bu = backup[0]
    print(bu)
    return(bu)

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("span.span-hotline")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    if(backup == []):
        bu2 = "-"
    else:
        bu = backup[0]
        bu0 = bu[0:10]
        bu1 = bu0.replace(",","")
        bu2 = bu1.replace(" ","")
    print(bu2)
    return(bu2)

def get_Location(soup): #จังหวัด
    detail = soup.select("div.date")
    j=0
    k=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split(' '))
        j=j+1
    for i in backup[0]:
        k+=1
    if(k == 4):
        bu = backup[0][3]
    else:
        bu = "-"
    print(bu)
    return bu

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("div.date")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split(' '))
        j=j+1
    #print(backup[0])
    dd = backup[0][0]
    mm = backup[0][1]
    yy = backup[0][2].replace(",","")

    months = ['ม.ค','ก.พ','มี.ค','เม.ย','พ.ค','มิ.ย','ก.ค','ส.ค','ก.ย','ต.ค','พ.ย','ธ.ค']
    for i in months:
        if i == mm:
            mm = str(months.index(i)+1)

    fulldate = (yy +'-'+ mm +'-'+dd)
    print(fulldate)
    return(fulldate)

def Main(links):
    r = requests.get(links)
    soup = BeautifulSoup(r.text, "lxml")
    CarDetail = {}
    CarDetail['pri'] = get_Price(soup)
    CarDetail['typ'] = get_TypeCar(soup)
    CarDetail['bra'] = get_Brand(soup)
    CarDetail['mod'] = get_Model(soup)
    CarDetail['yea'] = get_Year(soup)
    CarDetail['col'] = get_Color(soup)
    CarDetail['gea'] = get_Gear(soup)
    CarDetail['mil'] = get_Mileage(soup)
    CarDetail['nam'] = get_Seller(soup)
    CarDetail['tel'] = get_SellTel(soup)
    CarDetail['loc'] = get_Location(soup)
    CarDetail['dat'] = get_Date(soup)

Main('https://unseencar.com/taladrod/toyota-vios-trd-year-2014/1-5-2014-%E0%B8%A3%E0%B8%96%E0%B9%80%E0%B8%81%E0%B9%8B%E0%B8%87-4-%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%95%E0%B8%B9-aid277232')
Main('https://unseencar.com/taladrod/honda-jazz-sv-year-2013/1-5-i-vtec-%E0%B8%9B%E0%B8%B5-2013-aid277322')
Main('https://unseencar.com/taladrod/bmw-116i-year-2014/ปี-2014-รถเก๋ง-5-ประตู-aid277862')
Main('https://unseencar.com/taladrod/toyota-vios-e-year-2016/1-5-โฉมปี-13-17-aid275692')
Main('https://unseencar.com/taladrod/mitsubishi-triton-glx-year-2016/ปี-15-18-2-5-mega-cab-aid275572')
Main('https://unseencar.com/taladrod/nissan-x-trail-v-year-2016/2-0-โฉมปี-14-17-aid275602')
Main('https://unseencar.com/taladrod/nissan-np300-year-2018/navara-14-18-2-5-s-king-cab-aid275612')
Main('https://unseencar.com/taladrod/isuzu-d-max-sx-year-2008/05-12-2-5-d-di-i-teq-space-cab-aid275282')
Main('https://unseencar.com/taladrod/chevrolet-optra-year-2008/5dr-1-6-vgis-estate-ปี-08-10-aid31952')
Main('https://unseencar.com/taladrod/toyota-fortuner-v-4wd-year-2006/v-ปี-2006-aid266212')
Main('https://unseencar.com/taladrod/toyota-avanza-year-2016/1-5-e-โฉมปี-12-15-aid151422')
