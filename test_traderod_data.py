import requests
from bs4 import BeautifulSoup

def get_Price(soup): #ราคา
    detail = soup.select("h1.red")
    j=0
    backup=[]
    for i in detail:
        backup = i.text.strip().split(' ')
        j=j+1
    #print(backup)
    bu = backup[2]
    bu1 = bu.replace(",","")
    print(bu1)
    return(bu1)

def get_TypeCar(soup): #ประเภทรถ
    bu = "-"
    print(bu)
    return(bu)

def get_Brand(soup): #ยี่ห้อ
    detail = soup.select("table.table td")
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

def get_Model(soup): #รุ่น
    detail = soup.select("table.table td")
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

def get_Year(soup): #รุ่นปี
    detail = soup.select("table.table td")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[14]
    print(bu)
    return(bu)

def get_Color(soup): #สีรถ
    detail = soup.select("table.table td")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[23]
    bu1 = "สี"+bu
    print(bu1)
    return(bu1)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("table.table td")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[32]
    if(bu == "Manual"):
        bu1 = "เกียร์ธรรมดา"
    elif(bu == "Automatic"):
        bu1 = "เกียร์อัตโนมัติ"
    print(bu1)
    return(bu1)

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("table.table td")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[26]
    bu1 = bu.replace("km","")
    bu2 = bu1.replace(" ","")
    print(bu2)
    return(bu2)

def get_SellName(soup): #ชื่อผู้ขาย
    detail = soup.select("div.name_profile a")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[0]
    print(bu)
    return(bu)

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("div.name_profile ")
    j=0
    k=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    #print(backup)
    #for i in backup:
    #    k+=1
    #print(k)
    #print(backup[0][2].split(' '))
    #if(k == 1):
    bu = backup[0][2].replace(" ","")
    #else:
    #    bu = backup[0][2].replace(" ","")
    print(bu)
    return(bu)

def get_Location(soup): #จังหวัด
    detail = soup.select("table.table td")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[17]
    print(bu)
    return(bu)

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("table.table td")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    #print(backup)
    bu = backup[50]
    bu1 = bu.split(" ")
    dd = bu1[0]
    mm = bu1[1]
    yy = (int(bu1[2])+2500)
    yy1 = str(yy)

    months = ['ม.ค.','ก.พ.','มี.ค.','เม.ย.','พ.ค.','มิ.ย.','ก.ค.','ส.ค.','ก.ย.','ต.ค.','พ.ย.','ธ.ค.']
    for i in months:
        if i == mm:
            mm = str(months.index(i)+1)

    fulldate = (yy1 +'-'+ mm +'-'+ dd)
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

Main('https://www.traderod.com/cars/view.php?id_car=66634')
Main('https://www.traderod.com/cars/view.php?id_car=66606')
Main('https://www.traderod.com/cars/view.php?id_car=66054')
#Main('')
#Main('')
#Main('')
