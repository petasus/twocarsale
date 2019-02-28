import requests
from bs4 import BeautifulSoup

def get_Price(soup): #ราคา
    detail = soup.select("div.tab-content p.font-thaisans")
    j=0
    backup=[]
    backup1=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
        #print(backup[0][1].split(' '))
        backup1=backup[0][1].split(' ')
    #print(backup1[1])

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("div.tab-pane div.row div.col-md-6 p.font-thaisans")
    j=0
    backup2=[]
    backup3=[]
    for i in detail:
        backup2.append(i.text.strip().split('\n'))
        j=j+1
        #print(backup2)
        backup3=backup2[0][1]
    print(backup2[1][3])

#def get_Branch(soup): #ยี่ห้อ
#    detail = soup.select("div span[itemprop='manufacturer']")
#    for i in detail:
#        return (i.text.strip())
        #print (i.text.strip()) #ยังไม่ได้ส่งค่า แค่ปริ้นดูสิ่งที่ต้องการ

#def get_Model(soup): #รุ่น
#    detail = soup.select("div span[itemprop='model']")
#    for i in detail:
#        return (i.text.strip())
#        #print (i.text.strip())

#def get_Year(soup): #รุ่นปี
#    detail = soup.select("div span.float--right")
#    j=0
#    for i in detail:
#        j+=1
#        if j == 6:
#            return (i.text.strip())
            #print (i.text.strip())

#def get_Color(soup): #สีรถ
#    detail = soup.select("div span.float--right")
#    j=0
#    for i in detail:
#        j+=1
#        if j == 11:
#            return (i.text.strip())
            #print (i.text.strip())

#def get_Size(soup): #ขนาดเครื่องยนต์
#    detail = soup.select("div span.float--right")
#    j=0
#    for i in detail:
#        j+=1
#        if j == 7:
#            return (i.text.strip())
            #print (i.text.strip())

#def get_Gear(soup): #ระบบเกียร์
#    detail = soup.select("div span.float--right")
#    j=0
#    for i in detail:
#        j+=1
#        if j == 8:
#            return (i.text.strip())
            #print (i.text.strip())

#def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
#    detail = soup.select("div span.float--right")
#    j=0
#    for i in detail:
#        j+=1
#        if j == 10:
#            return (i.text.strip())
            #print (i.text.strip())

#def get_Location(soup):
#    detail = soup.select("div [style='border: 0']")
#    for i in detail:
#        return (i.text.strip())
        #print (i.text.strip())

#def get_Date(soup): #วันที่อัพเดท
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

#    CarDetail['branch_name'] = get_Branch(soup)
#    CarDetail['models'] = get_Model(soup)
#    CarDetail['years'] = get_Year(soup)
#    CarDetail['sizes'] = get_Size(soup)
#    CarDetail['gears'] = get_Gear(soup)
#    CarDetail['miles'] = get_Mileage(soup)
#    CarDetail['colors'] = get_Color(soup)
#    CarDetail['locates'] = get_Location(soup)
#    CarDetail['update_date'] = get_Date(soup)

Main('https://gucars.com/used-car/TOYOTA-CAMRY-2006/46965')
