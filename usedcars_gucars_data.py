import requests
from bs4 import BeautifulSoup

def get_Price(soup): #ราคา
    detail = soup.select("div.tab-content p.font-thaisans")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        #print(backup[0][1].split(' '))
        backup2=backup[0][1].split(' ')
    #print(backup2[1])

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("div.tab-content p.font-thaisans")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        #print(backup[1][3].split(' '))
        #backup2=backup[1][3]
    #print(backup2)

def get_Branch(soup): #ยี่ห้อ
    detail = soup.select("div.tab-content p.font-thaisans")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        #print(backup[0][2].split(' '))
        backup1=backup[0][2].split(' ')
    #print(backup1[1])

def get_Model(soup): #รุ่น
    detail = soup.select("div.tab-content p.font-thaisans")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        #print(backup[0][3].split(' '))
        backup2=backup[0][3].split(' ')
    #print(backup2[1])

def get_Year(soup): #รุ่นปี
    detail = soup.select("div.tab-content p.font-thaisans")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        #print(backup[0][4].split(' '))
        backup2=backup[0][4].split(' ')
    #print(backup2[1])

def get_Color(soup): #สีรถ
    detail = soup.select("div.tab-content p.font-thaisans")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        #print(backup[1][2].split(' '))
        #backup2=backup[1][2].split(' ')
    #print(backup2[1])

def get_Engine(soup): #ขนาดเครื่องยนต์
    detail = soup.select("div.tab-content p.font-thaisans")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        #print(backup[0][5].split(' '))
        backup2=backup[0][5].split(' ')
    #print(backup2[1])

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.tab-content p.font-thaisans")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        #print(backup[1][0].split(' '))
        #backup2=backup[1][0].split(' ')
    #print(backup2[1])

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div.tab-content p.font-thaisans")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        #print(backup[1][1].split(' '))
        #backup2=backup[1][1].split(' ')
    #print(backup2[1])

def get_SaleName(soup): #ชื่อผู้ขาย
    detail = soup.select("div.tab-content p.font-thaisans")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        #print(backup[1][1].split(' '))
        #backup2=backup[1][1].split(' ')
    #print(backup2[1])

def get_SaleTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("div.tab-content p.font-thaisans")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        #print(backup[1][1].split(' '))
        #backup2=backup[1][1].split(' ')
    #print(backup2[1])

def get_Location(soup): #จังหวัด
    detail = soup.select("div.tab-content p.font-thaisans")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        #print(backup[1][1].split(' '))
        #backup2=backup[1][1].split(' ')
    #print(backup2[1])

#def get_Update(soup): #วันที่อัพเดท
#    detail = soup.select("div.listing__updated.visuallyhidden--palm")
#    months = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
#    cutdate = detail[0].text.split(' ')
#    cutdate.remove(cutdate[0])
#    for i in months:
#        if i == cutdate[1]:
#            cutdate[1]=str(months.index(i)+1)
#    #print('/'.join(cutdate))
#    fulldate = ('/'.join(cutdate))
#    return (fulldate)
    #print (fulldate)

    #for i in detail:
    #date = str(detail)
    #date2= date[66:83]
    #print(date.split())
        #print (i.text.split())

def Main(links):
    r = requests.get(links)
    soup = BeautifulSoup(r.text, "lxml")
    cars_detail = []
    CarDetail = {}
    CarDetail['prices'] = get_Price(soup)
    CarDetail['types'] = get_TypeCar(soup)
    CarDetail['branchs'] = get_Branch(soup)
    CarDetail['models'] = get_Model(soup)
    CarDetail['years'] = get_Year(soup)
    CarDetail['colors'] = get_Color(soup)
    CarDetail['engines'] = get_Engine(soup)
    CarDetail['gears'] = get_Gear(soup)
    CarDetail['miles'] = get_Mileage(soup)
    CarDetail['names'] = get_SaleName(soup)
    CarDetail['tels'] = get_SaleTel(soup)
    CarDetail['locations'] = get_Location(soup)
#    CarDetail['updates'] = get_Update(soup)

Main('https://gucars.com/used-car/TOYOTA-CAMRY-2006/46965')
