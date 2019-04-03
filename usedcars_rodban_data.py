import requests
from bs4 import BeautifulSoup

def get_Price(soup): #ราคา
    detail = soup.select("div.car_characteristics div.price")
    j=0
    backup=[]
    for i in detail:
        backup = i.text.strip().split(' ')
        j=j+1
    bu = backup[1]
    bu1 = bu.replace("บาท","")
    bu2 = bu1.replace(",","")
    bu3 = bu2.replace("\t","")
    print(bu3)
    return(bu3)

def get_TypeCar(soup): #ประเภทรถ
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        backup2=backup[0][0].split('\t')
        j=j+1
    bu = backup2[0]
    #print(bu)
    bu1 = "รถ" + bu
    if(bu == "แวน"):
        bu1 = "รถตู้"
    elif(bu == "รถทั้งหมด"):
        bu1 = "-"
    print(bu1)
    return(bu1)

def get_Brand(soup): #ยี่ห้อ
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        backup2=backup[0][0].split('\t')
        j=j+1
    bu = backup2[1]
    bu1 = bu.replace(",","")
    bu2 = bu1.replace(" ","")
    bu3 = (bu2.lower())
    print(bu3)
    return(bu3)

def get_Model(soup): #รุ่น
    detail = soup.select("div.features_table div.right")
    j=0
    a=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        backup2=backup[0][0].split('\t')
        j=j+1
    #print(backup2)
    for i in backup2:
        a=a+1
    if (a == 2):
        bu2 = "-"
    else:
        bu = backup2[2].split(' ')
        bu1 = bu[1]
        bu2 = (bu1.lower())
        #bu1 = bu.replace(",","")
        #bu2 = bu1.replace(" ","")
    print(bu2)
    return(bu2)

def get_Year(soup): #รุ่นปี
    detail = soup.select("div.features_table div.right")
    j=0
    a=0
    b=0
    backup=[]
    backup2=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
        j=j+1
    #print(backup[0])
    for i in backup[0]:
        a = a+1
    #print(a)
    if(a == 5):
        backup2=backup[0][4].split('\t')
        #print(backup2)
        bu = backup2[5]
        bu1 = bu.replace(" ","")
    elif(a == 4):
        backup2=backup[0][3].split('\t')
        #print(backup2)
        for i in backup2:
            b+=1
        bu = backup2[b-1]
        bu1 = bu.replace(" ","")
    else:
        backup2=backup[0][3].split('\t')
        #print(backup2)
        bu = backup2[3]
        bu1 = bu.replace(" ","")
    print(bu1)
    return(bu1)

def get_Color(soup): #สีรถ
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    print("สี"+backup[5])
    return("สี"+backup[5])


def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[4]
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
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[3]
    if(bu == "ไม่ระบุเลขไมล์"):
        bu4 = "-"
    elif(bu == "ไม่เกิน 5,000 km"):
        bu4 = "<5000"
    elif(bu == "มากกว่า 500,000 km"):
        bu4 = ">500000"
    else:
        bu1 = bu.replace("km","")
        bu2 = bu1.replace(" ","")
        bu3 = bu2.replace(",","")
        bu4 = bu3
        #bu5 = bu4[0]+bu4[1]+bu4[2]+bu4[3]+bu4[4]
        #bu6 = bu4[5]+bu4[6]+bu4[7]+bu4[8]+bu4[9]
        #bu7 = (int(bu5)+int(bu6))/2
    print(bu4)
    return(bu4)

def get_SellName(soup): #ชื่อผู้ขาย
    detail = soup.select("div.author span")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[0]
    print(bu)
    return(bu)

def get_SellTel(soup): #เบอร์ผู้ขาย
    detail = soup.select("div.phones div.pointer")
    j=0
    backup=[]
    for i in detail:
        backup.append(i)
        j=j+1
    bu = str(backup)
    if(bu[74] == "\\"):
        bu1 = bu[65]+bu[66]+bu[67]+bu[68]+bu[69]+bu[70]+bu[71]+bu[72]+bu[73]+""
    else:
        bu1 = bu[65]+bu[66]+bu[67]+bu[68]+bu[69]+bu[70]+bu[71]+bu[72]+bu[73]+bu[74]
    print(bu1)
    return(bu1)

def get_Location(soup): #จังหวัด
    detail = soup.select("div.right a")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[1]
    print(bu)
    return(bu)

def get_Date(soup): #วันที่อัพเดท
    detail = soup.select("div.features_table div.right")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
        j=j+1
    bu = backup[7].split(" ")
    if(bu[1] == "นาทีที่แล้ว" or bu[1] == "ชั่วโมงที่แล้ว" or bu[0] == "เมื่อวาน"):
        dd = "20"
        mm = "เมษายน"
        yy = "2562"
    else:
        dd = bu[0]
        mm = bu[1]
        yy = bu[2].replace(",","")

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

#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/toyotacamry-138983.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/suzukiswift-143442.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/mitsubishi-143441.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/toyotahiace-143367.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/hondajazz-143307.html')
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/isuzud-max-%E0%B8%9B%E0%B8%B512-15-143542.html')

#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/toyotacamry-144804.html') #year
#Main('https://xn--22caobb7fvah1fc9id1dce1ti4me.net/toyotahilux-vigo-144808.html')
