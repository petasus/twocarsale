import requests
from bs4 import BeautifulSoup

def get_Price(soup): #ราคา
    detail = soup.select("div.grid__item div.listing__price")
    j=0
    backup=[]
    for i in detail:
        backup = i.text.strip().split(' ')
        j=j+1
    #print(backup[0])
    bu = backup[0]
    bu1 = bu.replace(",","")
    print(bu1)
    return(bu1)

def get_TypeCar(soup): #ประเภทรถ
    bu = "-"
    print(bu)
    return bu

def get_Brand(soup): #ยี่ห้อ
    detail = soup.select("div.listing__key-listing__list span.float--right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[1]
    bu1 = (bu.lower())
    print(bu1)
    return(bu1)

def get_Model(soup): #รุ่น
    detail = soup.select("div.listing__key-listing__list span.float--right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[2]
    bu1 = (bu.lower())
    print(bu1)
    return(bu1)

def get_Year(soup): #รุ่นปี
    detail = soup.select("div.listing__key-listing__list span.float--right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[5]
    bu1 = (bu.lower())
    print(bu1)
    return(bu1)

def get_Color(soup): #สีรถ
    detail = soup.select("div.listing__key-listing__list span.float--right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[10]
    print(bu)
    return(bu)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.listing__key-listing__list span.float--right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[7]
    print(bu)
    return(bu)

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div.listing__key-listing__list span.float--right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[9]
    print(bu)
    return(bu)

def get_SellName(soup): #ชื่อผู้ขาย
    detail = soup.select("div.modal__body")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    print(backup)
    #bu = backup[8]
    #print(bu)
    #return(bu)

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("div.flexbox__row div.flexbox__item a")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    #bu = backup[0]
    #print(bu)
    #return(bu)

def get_Location(soup): #จังหวัด
    detail = soup.select("div.list-item ")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    backup2 = backup[1].split(' ')
    bu = backup2[146]
    print(bu)
    return(bu)

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("div.listing__updated")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[0].split(' ')
    #if(bu[1] == "นาทีที่แล้ว" or bu[1] == "ชั่วโมงที่แล้ว" or bu[0] == "เมื่อวาน"):
        #dd = "26"
        #mm = "มีนาคม"
        #yy = "2562"
    #else:
    dd = bu[1]
    mm = bu[2]
    yy = bu[3]

    months = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
    for i in months:
        if i == mm:
            mm = str(months.index(i)+1)

    fulldate = (yy +'-'+ mm +'-'+ dd)
    print(fulldate)
    return(fulldate)

def Main(links):
    r = requests.get(links)
    soup = BeautifulSoup(r.text, "lxml")
    cars_detail = []
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

#Main('https://www.one2car.com/for-sale/toyota-yaris-ace-%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%9B%E0%B8%A3%E0%B8%B4%E0%B8%A1%E0%B8%93%E0%B8%91%E0%B8%A5-%E0%B8%81%E0%B8%B2%E0%B8%8D%E0%B8%88%E0%B8%99%E0%B8%B2%E0%B8%A0%E0%B8%B4%E0%B9%80%E0%B8%A9%E0%B8%81/5676000')
#Main('https://www.one2car.com/for-sale/toyota-hilux-revo-e-%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%9B%E0%B8%A3%E0%B8%B4%E0%B8%A1%E0%B8%93%E0%B8%91%E0%B8%A5-%E0%B8%9B%E0%B8%B4%E0%B9%88%E0%B8%99%E0%B9%80%E0%B8%81%E0%B8%A5%E0%B9%89%E0%B8%B2-%E0%B8%96%E0%B8%99%E0%B8%99%E0%B8%9A%E0%B8%A3%E0%B8%A1%E0%B8%A3%E0%B8%B2%E0%B8%8A%E0%B8%8A%E0%B8%99%E0%B8%99%E0%B8%B5/5484208')
Main('https://www.one2car.com/for-sale/toyota-hilux-vigo-e-prerunner-%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%9B%E0%B8%A3%E0%B8%B4%E0%B8%A1%E0%B8%93%E0%B8%91%E0%B8%A5-%E0%B8%AD%E0%B8%B3%E0%B9%80%E0%B8%A0%E0%B8%AD%E0%B8%AA%E0%B8%B2%E0%B8%A1%E0%B9%82%E0%B8%84%E0%B8%81/5729306#2102468613')
#Main('')
#Main('')
#Main('')
