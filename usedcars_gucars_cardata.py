import requests
from bs4 import BeautifulSoup

def get_Branch(soup): #ยี่ห้อ
    detail = soup.select("div span[itemprop='manufacturer']")
    for i in detail:
        return (i.text.strip())
        #print (i.text.strip()) #ยังไม่ได้ส่งค่า แค่ปริ้นดูสิ่งที่ต้องการ

def get_Model(soup): #รุ่น
    detail = soup.select("div span[itemprop='model']")
    for i in detail:
        return (i.text.strip())
        #print (i.text.strip())

def get_Genre(soup): #โฉมรถยนต์
    detail = soup.select("div span.float--right")
    j=0
    for i in detail:
        j+=1
        if j == 4:
            return (i.text.strip())
            #print (i.text.strip())

def get_DetailModel(soup): #รายละเอียดรุ่น
    detail = soup.select("div span.float--right")
    j=0
    for i in detail:
        j+=1
        if j == 5:
            return (i.text.strip())
            #print (i.text.strip())

def get_Year(soup): #รุ่นปี
    detail = soup.select("div span.float--right")
    j=0
    for i in detail:
        j+=1
        if j == 6:
            return (i.text.strip())
            #print (i.text.strip())

def get_Size(soup): #ขนาดเครื่องยนต์
    detail = soup.select("div span.float--right")
    j=0
    for i in detail:
        j+=1
        if j == 7:
            return (i.text.strip())
            #print (i.text.strip())

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div span.float--right")
    j=0
    for i in detail:
        j+=1
        if j == 8:
            return (i.text.strip())
            #print (i.text.strip())

def get_Mileage(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div span.float--right")
    j=0
    for i in detail:
        j+=1
        if j == 10:
            return (i.text.strip())
            #print (i.text.strip())

def get_Color(soup): #สีรถ
    detail = soup.select("div span.float--right")
    j=0
    for i in detail:
        j+=1
        if j == 11:
            return (i.text.strip())
            #print (i.text.strip())

def get_Price(soup): #ราคา
    detail = soup.select("div.grid__item.five-twelfths.lap-one-half.visuallyhidden--palm.text--right div.listing__price.delta.weight--bold")
    #detail = soup.select("div.listing__summarybar.element-sticky-bottom.no-print div div div div div div div.listing__price.delta.weight--bold")
    for i in detail:
        return (i.text.strip())
        #print (i.text.strip())

def get_Location(soup):
    detail = soup.select("div [style='border: 0']")
    for i in detail:
        return (i.text.strip())
        #print (i.text.strip())

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("div.listing__updated.visuallyhidden--palm")
    months = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
    cutdate = detail[0].text.split(' ')
    cutdate.remove(cutdate[0])
    for i in months:
        if i == cutdate[1]:
            cutdate[1]=str(months.index(i)+1)
    #print('/'.join(cutdate))
    fulldate = ('/'.join(cutdate))
    return (fulldate)
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
    CarDetail['branch_name'] = get_Branch(soup)
    CarDetail['models'] = get_Model(soup)
    CarDetail['genres'] = get_Genre(soup)
    CarDetail['detail_model'] = get_DetailModel(soup)
    CarDetail['years'] = get_Year(soup)
    CarDetail['sizes'] = get_Size(soup)
    CarDetail['gears'] = get_Gear(soup)
    CarDetail['miles'] = get_Mileage(soup)
    CarDetail['colors'] = get_Color(soup)
    CarDetail['prices'] = get_Price(soup)
    CarDetail['locates'] = get_Location(soup)
    CarDetail['update_date'] = get_Date(soup)

#Main('https://www.one2car.com/for-sale/ford-ranger-hi-rider-xlt-%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%9B%E0%B8%A3%E0%B8%B4%E0%B8%A1%E0%B8%93%E0%B8%91%E0%B8%A5-%E0%B8%81%E0%B8%B2%E0%B8%8D%E0%B8%88%E0%B8%99%E0%B8%B2%E0%B8%A0%E0%B8%B4%E0%B9%80%E0%B8%A9%E0%B8%81/4815426')
