import requests
from bs4 import BeautifulSoup

def get_Price(soup): #ราคา
    detail = soup.select("div.left-content p.price")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split(' '))
        j=j+1
    bu = backup[0][0]
    bu1 = bu.replace(",","")
    #print(bu1)
    return(bu1)

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    for i in backup:
        if(i == "ประเภทรถ" ):
            a = k+1
        k=k+1
    if(a != 1000):
        bu = (backup[a].lower())
    else:
        bu = "-"
    if(bu == "รถเก๋ง 4 ประตู"):
        bu1 = "รถเก๋ง"
    elif(bu == "SUV"):
        bu1 = "รถSUV"
    elif(bu == "Truck"):
        bu1 = "รถบรรทุก"
    elif(bu == "Wagon" or bu == "รถเก๋ง 5 ประตู"):
        bu1 = "รถอเนกประสงค์"
    elif(bu == "รถตู้/MPV" or bu == "รถตู้/VAN"):
        bu1 = "รถตู้"
    elif(bu == "รถเก๋ง 2 ประตุ" or bu == "รถเปิดประทุน" or bu == "Cabriolet"):
        bu1 = "รถสปอร์ต"
    else:
        bu1 = bu
    #print(bu1)
    return(bu1)

def get_Brand(soup): #ยี่ห้อ
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    for i in backup:
        if(i == "ยี่ห้อ" ):
            a = k+1
        k=k+1
    if(a != 1000):
        bu = (backup[a].lower())
    else:
        bu = "-"
    #print(bu)
    return(bu)

def get_Model(soup): #รุ่น
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    for i in backup:
        if(i == "รุ่น" ):
            a = k+1
        k=k+1
    if(a != 1000):
        bu = (backup[a].lower())
    else:
        bu = "-"
    #print(bu)
    return(bu)

def get_Year(soup): #รุ่นปี
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    for i in backup:
        if(i == "ปีที่ผลิต" ):
            a = k+1
        k=k+1
    if(a != 1000):
        bu = backup[a]
    else:
        bu = "-"
    #print(bu)
    return(bu)

def get_Color(soup): #สีรถ
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    for i in backup:
        if(i == "สี" ):
            a = k+1
        k=k+1
    if(a != 1000):
        bu = backup[a]
    else:
        bu = "-"
    #print(bu)
    return(bu)

#def get_Engine(soup): #ขนาดเครื่องยนต์
    #detail = soup.select("div.row div.col-lg-4")
    #j=0
    #backup=[]
    #backup2=[]
    #for i in detail:
        #backup.append(i.text.strip().split('\n'))
        #j=j+1
        #backup2=backup[0][18].split(' ')
    #print(backup2[0])

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    for i in backup:
        if(i == "ระบบส่งกำลัง" ):
            a = k+1
        k=k+1
    if(a != 1000):
        bu = backup[a]
    else:
        bu = "-"
    #print(bu)
    return(bu)

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=0
    a=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    for i in backup:
        if(i == "เลขไมล์" ):
            a=k+1
        k=k+1
    if(a != 1000):
        bu = backup[a]
        bu1 = bu.replace(",","")
    else:
        bu = "-"
    #print(bu1)
    return(bu1)

def get_SellName(soup): #ชื่อผู้ขาย
    detail = soup.select("div.col-box h4")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[0]
    #print(bu)
    return(bu)

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("div.col-box span")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[0].replace(".","")
    #print(bu)
    return(bu)

def get_Location(soup): #จังหวัด
    detail = soup.select("div.title-page p.info-title")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[0].replace("|","")
    bu1 = bu.split(" ")
    bu2 = bu1[0]
    #print(bu2)
    return(bu2)

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("div.title-page p.info-title")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[0].replace("|","")
    bu1 = bu.split(" ")
    dd = bu1[2]
    mm = bu1[3]
    yy = bu1[4]

    months = ['ม.ค','ก.พ','มี.ค','เม.ย','พ.ค','มิ.ย','ก.ค','ส.ค','ก.ย','ต.ค','พ.ย','ธ.ค']
    for i in months:
        if i == mm:
            mm = str(months.index(i)+1)

    fulldate = (yy +'-'+ mm +'-'+dd)
    #print(fulldate)
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
    #CarDetail['eng'] = get_Engine(soup)
    CarDetail['gea'] = get_Gear(soup)
    CarDetail['mil'] = get_Mileage(soup)
    CarDetail['nam'] = get_SellName(soup)
    CarDetail['tel'] = get_SellTel(soup)
    CarDetail['loc'] = get_Location(soup)
    CarDetail['dat'] = get_Date(soup)

#Main('https://rodmuesong.com/%E0%B8%A3%E0%B8%96%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%82%E0%B8%B2%E0%B8%A2/chevrolet-colorado-year-2011/%E0%B8%82%E0%B8%B2%E0%B8%A2%E0%B8%A3%E0%B8%96-%E0%B8%97%E0%B8%B5%E0%B9%88-%E0%B8%8A%E0%B8%A5%E0%B8%9A%E0%B8%B8%E0%B8%A3%E0%B8%B5-aid7097521')
