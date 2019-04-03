import requests
from bs4 import BeautifulSoup

def get_Price(soup): #ราคา
    detail = soup.select("p.price span")
    backup=[]
    j=0
    for i in detail:
        backup.append(i.text.strip().split(' '))
        j=j+1
    bu = backup[0][1]
    bu1 = bu.replace(",","")
    #print(int(bu1))

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("div.section-body")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    if(backup[0][44] == "Pickup"):
        bu = "รถกระบะ"
        #print(bu)
    elif(backup[0][44] == "Sedan"):
        bu = "รถเก๋ง"
        #print(bu)
    elif(backup[0][44] == "SUV"):
        bu = "รถSUV"
        #print(bu)
    elif(backup[0][44] == "VAN"):
        bu = "รถตู้"
        #print(bu)
    elif(backup[0][44] == "Hatchback"):
        bu = "รถแฮชท์แบค"
        #print(bu)
    elif(backup[0][44] == "Wagon/Minivan"):
        bu = "รถมินิแวน"
        #print(bu)
    elif(backup[0][44] == "Coupe/Convertible"):
        bu = "รถเปิดประทุน"
        #print(bu)
    elif(backup[0][44] == "Other"):
        bu = "อื่นๆ"
        #print(bu)

def get_Brand(soup): #ยี่ห้อ
    detail = soup.select("div.section-body")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    #print(backup[0][4])

def get_Model(soup): #รุ่น
    detail = soup.select("div.section-body")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    #print(backup[0][14])

def get_Year(soup): #รุ่นปี
    detail = soup.select("div.section-body")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    #print(backup[0][35])

def get_Color(soup): #สีรถ
    detail = soup.select("div.section-body")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    #print(backup[0][40])


def get_Engine(soup): #ขนาดเครื่องยนต์
    detail = soup.select("div.section-body")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    bu = backup[0][61]
    bu1 = bu.replace(" ","")
    bu2 = bu1.replace("CC","")
    #print(bu2)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.section-body")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    if(backup[0][73] == "manual"):
        bu = "เกียร์ธรรมดา"
        #print(bu)
    elif(backup[0][73] == "Auto"):
        bu = "เกียร์อัตโนมัติ"
        #print(bu)

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div.section-body")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    bu = backup[0][57]
    bu1 = bu.replace("km","")
    bu2 = bu1.replace("-","")
    bu3 = bu2.replace(",","")
    bu4 = bu3.replace(" ","")
    bu5 = bu4[0]+bu4[1]+bu4[2]+bu4[3]+bu4[4]
    bu6 = bu4[5]+bu4[6]+bu4[7]+bu4[8]+bu4[9]
    bu7 = (int(bu5)+int(bu6))/2
    #print(bu7)

def get_SellName(soup): #ชื่อผู้ขาย
    detail = soup.select("div.seller-menu")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    #print(backup[0][2])

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("div.seller-menu")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    bu = backup[0][7]
    bu1 = bu.replace(" ","")
    bu2 = bu1.replace("|","")
    bu3 = bu2.replace("\xa0","")
    #print(bu3)

def get_Location(soup): #จังหวัด
    detail = soup.select("div.seller-menu")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    bu = backup[0][8]
    #print(bu.replace(" ",""))


def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("div.section-body")
    months = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
#    cutdate = detail[0].text.split(' ')
#    cutdate.remove(cutdate[0])
#    for i in months:
#        if i == cutdate[1]:
#            cutdate[1]=str(months.index(i)+1)
#    print('/'.join(cutdate))
#    fulldate = ('/'.join(cutdate))
#    return (fulldate)
#    print (fulldate)

#    for i in detail:
#     date = str(detail)
#     date2= date[66:83]
#     print(date.split())
#     print (i.text.split())

def Main(links):
    r = requests.get(links)
    soup = BeautifulSoup(r.text, "lxml")
    cars_detail = []
    CarDetail = {}
    CarDetail['pri'] = get_Price(soup)
    CarDetail['typ'] = get_TypeCar(soup)
    CarDetail['bra'] = get_Brand(soup)
    CarDetail['mod'] = get_Model(soup)
    CarDetail['yea'] = get_Year(soup)
    CarDetail['col'] = get_Color(soup)
    CarDetail['eng'] = get_Engine(soup)
    CarDetail['gea'] = get_Gear(soup)
    CarDetail['mil'] = get_Mileage(soup)
    CarDetail['sel'] = get_SellName(soup)
    CarDetail['tel'] = get_SellTel(soup)
    CarDetail['loc'] = get_Location(soup)
    CarDetail['dat'] = get_Date(soup)

Main('http://www.thaicar.com/used-cars/d400059/toyota-hilux-vigo-champ-smart-cab-11-15-/')
