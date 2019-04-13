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
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    #print(backup)
    if(backup[0][14] == "ประเภทรถ"):
        bu = backup[0][15]
    else:
        bu = backup[0][17]

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
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    #print(backup)
    if(backup[0][4] == "ปีที่ผลิต"):
        bu = backup[0][5]
    else:
        bu = backup[0][7]
    print(bu)
    return(bu)

def get_Color(soup): #สีรถ
    detail = soup.select("div.main-tab ul")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    #print(backup)
    if(backup[0][12] == "สี"):
        bu = backup[0][13]
    else:
        bu = backup[0][15]
    print(bu)
    return(bu)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.main-tab ul")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    #print(backup)
    if(backup[0][8] == "ระบบส่งกำลัง"):
        bu = backup[0][9]
    else:
        bu = backup[0][11]
    if(bu == "ระบบส่งกำลัง"):
        bu1 = "-"
    print(bu1)
    return(bu1)

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div.main-tab ul")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    print(backup)
    if(backup[0][8] == "เลขไมล"):
        bu = backup[0][9]
    else:
        bu = backup[0][11]
    bu1 = bu.replace("km","")
    bu2 = bu1.replace(",","")
    bu3 = bu2.replace(" ","")
    print(bu3)
    return(bu3)

def get_SellName(soup): #ชื่อผู้ขาย
    detail = soup.select("div.info-c div.short-c")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\xa0'))
        j=j+1
    #print(backup)
    bu = backup[0][0].split(' ')
    bu1 = bu[1]
    if(bu1 == ''):
        bu4 = "-"
    else:
        bu2 = bu1.replace("\n","")
        bu3 = bu2.replace("\xa0","")
        bu4 = bu3.replace("\r"," ")
    print(bu4)
    return(bu4)

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("span.span-hotline")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[0]
    print(bu[0:10])
    return(bu[0:10])

def get_Location(soup): #จังหวัด
    detail = soup.select("div.date")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split(' '))
        j=j+1
    #print(backup[0])
    bu = backup[0][3]
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
    CarDetail['nam'] = get_SellName(soup)
    CarDetail['tel'] = get_SellTel(soup)
    CarDetail['loc'] = get_Location(soup)
    CarDetail['dat'] = get_Date(soup)

Main('https://unseencar.com/taladrod/toyota-vios-trd-year-2014/1-5-2014-%E0%B8%A3%E0%B8%96%E0%B9%80%E0%B8%81%E0%B9%8B%E0%B8%87-4-%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%95%E0%B8%B9-aid277232')
Main('https://unseencar.com/taladrod/honda-jazz-sv-year-2013/1-5-i-vtec-%E0%B8%9B%E0%B8%B5-2013-aid277322')
Main('https://unseencar.com/taladrod/bmw-116i-year-2014/ปี-2014-รถเก๋ง-5-ประตู-aid277862')
#Main('')
#Main('')
#Main('')
#Main('')
#Main('')
#Main('')
