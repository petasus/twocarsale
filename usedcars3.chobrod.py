import requests
from bs4 import BeautifulSoup
from upload_data import uploadToSql as uploadDB
import connect
import datetime
import time
keep_sendlink=[] #สร้างฟังก์ชั่นเก็บเว็บไซต์และส่งไปยังอีกไฟล์
keep_typelink=[]
keep_typename=[]
max_typecar=[]
db = connect.conDB()

def get_Type(num): #ประเภทรถ
    if(num == 1):
        ty = 'รถเก๋ง 4 ประตู'
    elif(num == 2):
        ty = 'รถกระบะ'
    elif(num == 3):
        ty = 'SUV'
    elif(num == 4):
        ty = 'รถเก๋ง 5 ประตู'
    elif(num == 5):
        ty = 'รถตู้/VAN'
    elif(num == 6):
        ty = 'รถเก๋ง 2 ประตู'
    elif(num == 7):
        ty = 'Wagon'
    elif(num == 8):
        ty = 'รถเปิดประทุน'
    elif(num == 9):
        ty = 'รถตู้/MPV'
    elif(num == 10):
        ty = 'Truck'
    elif(num == 11):
        ty = 'Cabriolet'
    elif(num == 12):
        ty = 'EV/Hybrid'
    else:
        ty = "-"
    print(ty)
    #while(True):
    #    CKsql = """ SELECT id FROM type_car WHERE `name`=%s"""
    #    c = db.cursor()
    #    CKExis = c.execute(CKsql,(ty))
    #    if CKExis:
    #        getID = c.fetchall()
    #        return getID[0][0]
    #    else:
    #        c.execute("""INSERT INTO type_car (`name`) VALUES (%s)""", (ty))
    #        db.commit()
    #        continue

def get_Brand(soup): #ยี่ห้อ
    detail = soup.select("ul.info-detail-prd span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == 'ยี่ห้อ'):
            k = j+1
        j=j+1
    if(k != 1000):
        br = backup[k]
    else:
        br = "-"
    print(br)
    #while(True):
    #    CKsql = """ SELECT id FROM brand WHERE `name`=%s"""
    #    c = db.cursor()
    #    CKExis = c.execute(CKsql,(br))
    #    if CKExis:
    #        getID = c.fetchall()
    #        return getID[0][0]
    #    else:
    #        c.execute("""INSERT INTO brand (`name`) VALUES (%s)""", (br))
    #        db.commit()
    #        continue

def get_Model(soup): #รุ่น
    detail = soup.select("ul.info-detail-prd span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == 'รุ่น'):
            k = j+1
        j=j+1
    if(k != 1000):
        mod = (backup[k].lower())
    else:
        mod = "-"
    print(mod)
    #TypeCar = get_TypeCar(soup)
    #Brand = get_Brand(soup)
    #Gear = get_Gear(soup)
    #while(True):
    #    CKsql = """ SELECT id FROM model WHERE `name`=%s AND `bnd_id`=%s AND `typ_id`=%s"""
    #    c = db.cursor()
    #    CKExis = c.execute(CKsql,(mo,Brand,TypeCar))
    #    if CKExis:
    #        getID = c.fetchall()
    #        return getID[0][0]
    #    else:
    #        c.execute("""INSERT INTO model (`name`,`bnd_id`,`typ_id`,`gears`) VALUES (%s,%s,%s,%s)""", (mo,Brand,TypeCar,Gear))
    #        db.commit()

def get_Submodel(soup): #รุ่นย่อย
    detail = soup.select("ul.info-detail-prd span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == 'รุ่นย่อย'):
            k = j+1
        j=j+1
    if(k != 1000):
        sm = (backup[k].lower())
    else:
        sm = "-"
    print(sm)

def get_Web(soup): #ชื่อเว็บ
    we = 'chobrod.com'
    print(we)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("ul.info-detail-prd span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == 'ระบบส่งกำลัง'):
            k = j+1
        j=j+1
    if(k != 1000):
        ge = backup[k]
    else:
        ge = "-"
    print(ge)

def get_Post(soup): #วันที่โพส
    detail = soup.select("div.colum-right b")
    backup=[]
    months = ['ม.ค','ก.พ','มี.ค','เม.ย','พ.ค','มิ.ย','ก.ค','ส.ค','ก.ย','ต.ค','พ.ย','ธ.ค']
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0].split(" ")
    dd = bu[0]
    mm = bu[1]
    yy = bu[2]
    for i in months:
        if i == mm:
            mm = str(months.index(i)+1)
            if(int(mm) <= 9 ):
                mm = "0"+str(mm)
    if(int(dd) <= 9 ):
        dd = "0"+str(dd)
    po = (yy +'-'+ mm +'-'+dd)
    print(po)

def get_Price(soup): #ราคา
    detail = soup.select("div.mg-bottom-20 span")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0]
    if(bu == "ติดต่อผู้ขาย"):
        pr = "0"
    else:
        bu1 = bu.replace("บาท","")
        bu2 = bu1.replace(",","")
        pr = bu2.replace(" ","")
    print(pr)

def get_Location(soup): #จังหวัด
    detail = soup.select("div.colum-right p")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0].split(" ")
    lo = bu[0]
    print(lo)

def get_Year(soup): #รุ่นปี
    detail = soup.select("ul.info-detail-prd span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == 'ปีที่ผลิต'):
            k = j+1
        j=j+1
    if(k != 1000):
        ye = backup[k]
    else:
        ye = "-"
    print(ye)

def get_Mile(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("ul.info-detail-prd span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == 'เลขไมล์ (กม.)'):
            k = j+1
        j=j+1
    if(k != 1000):
        bu = backup[k].replace(",","")
        bu1 = bu.replace(" ","")
        mi = bu1.replace("km","")
    else:
        mi = "-"
    print(mi)

def get_Color(soup): #สีรถ
    detail = soup.select("ul.info-detail-prd span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == 'สี'):
            k = j+1
        j=j+1
    if(k != 1000):
        co = backup[k]
    else:
        co = "-"
    print(co)

def get_Seller(soup): #ชื่อผู้ขาย
    detail = soup.select("div.box-detail-left span.name")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0]
    if(bu == ''):
        se = "-"
    else:
        se = bu
    print(se)

def get_Tel(soup): #เบอร์ผู้ขาย
    detail = soup.select("div.box-detail-left span.show-phone")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    if(backup == ['']):
        te = "-"
    else:
        te = backup[0]
    print(te)

def get_Place(soup): #ที่อยู่
    detail = soup.select("div.box-detail-left span")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    if(backup[4] == ''):
        pl = "-"
    else:
        pl = backup[4]
    print(pl)

def get_description(soup): #รายละเอียด
    detail = soup.select("div.pre-line")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    de = backup[0]
    print(de)

def get_specification(soup): #ข้อมูลจำเพาะทางเทคนิค
    detail = soup.select("ul li")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    print(backup)
    if(backup == []):
        sp = "ไม่มีข้อมูล"
    else:
        sp = backup[0]
    print(sp)

def get_Image(soup):
    detail = soup.select("div.content-listthumb img")
    j=0
    k=0
    im=""
    backup=[]
    for i in detail:
        backup.append(i['src'])
        j+=1
    if(j==0):
        im = "-"
    else:
        while(k != j):
            im += backup[k]+" "
            k+=1
    print(im)

def get_CheckUpdate(soup):
    detail = soup.select("div.title-page p.info-title")
    backup=[]
    months = ['ม.ค','ก.พ','มี.ค','เม.ย','พ.ค','มิ.ย','ก.ค','ส.ค','ก.ย','ต.ค','พ.ย','ธ.ค']
    for i in detail:
        backup.append(i.text.strip())
    print(backup)
    if(backup == []):
        chd = 0
    else:
        bu = backup[0].split(" ")
        dd = bu[2]
        mm = bu[3]
        yy = bu[4]
        yy = int(yy)-2543
        for i in months:
            if(i == mm):
                mm = str(months.index(i)+1)
                if(int(mm) <= 9 ):
                    mm = "0"+str(mm)
        if(int(dd) <= 9 ):
            dd = "0"+str(dd)
        day = str(mm)+"/"+str(dd)+"/"+str(yy)
        xx = datetime.datetime.now()
        xd = xx.strftime("%x")
        if(day == xd):
            chd = 0
        else:
            chd = 1
    print(chd)
    return(chd)

def get_ErrorCheck(soup):
    detail = soup.select("div.title h4.fweight-bold")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    if(backup == []):
        bu = 1
    else:
        bu = 0
    print(bu)
    return(bu)

def Main(links,tier,max):
    #Car_upload=[]
    j=1
    a=0
    for i in links:
        print("link no." + str(j) + " " + i)
        while True:
            try:
                r = requests.get(i)
                break
            except:
                print("มีปัญหากลับไปรีเควสใหม่")
                print("ที่ลิ้ง: "+str(i))
                time.sleep(10)
                continue
        soup = BeautifulSoup(r.text, "lxml")
        j+=1
        k=1
        a+=1
        CarDetail = {}
        CarDetail['err'] = get_ErrorCheck(soup)
        if(CarDetail['err']== 0):
            continue
        CarDetail['che'] = get_CheckUpdate(soup)
        if(CarDetail['che']== 0):
            continue
        #CarDetail['typ'] = get_Type(k)###
        #CarDetail['bra'] = get_Brand(soup)###
        #CarDetail['mod'] = get_Model(soup)###
        #CarDetail['sub'] = get_Submodel(soup)###
        #CarDetail['gea'] = get_Gear(soup)###
        #CarDetail['web'] = get_Web(soup)
        #CarDetail['pos'] = get_Post(soup)
        #CarDetail['pri'] = get_Price(soup)
        #CarDetail['loc'] = get_Location(soup)
        #CarDetail['yea'] = get_Year(soup)
        #CarDetail['mil'] = get_Mile(soup)
        #CarDetail['col'] = get_Color(soup)
        #CarDetail['sel'] = get_Seller(soup)
        #CarDetail['tel'] = get_Tel(soup)
        #CarDetail['pla'] = get_Place(soup)
        #CarDetail['des'] = get_description(soup)
        ###CarDetail['cla'] = get_description(soup)#อุบัติเหตุ ชน น้ำท่วม แต่ง ติดแก๊ส
        ###CarDetail['pro'] = get_description(soup)#โปรโมชั่น ส่วนลด ดาวน์
        ###CarDetail['ser'] = get_description(soup)#รับประกันหลังการขาย
        ##CarDetail['spe'] = get_specification(soup)##มีข้อมูลแต่เก็บไม่ได้
        CarDetail['img'] = get_Image(soup)
        ###CarDetail['dup'] = get_duplicate(soup) #check ซ้ำ
        ###CarDetail['upd'] = get_update(soup) #updatedatabase
        if(a == max[0]):
            max[0]+=max[k]
            k+=1
        #Car_upload.append(CarDetail)
    #uploadDB(Car_upload)

def getLink():
    print("Start getLink")
    url_to_type = 'https://chobrod.com/car-sale/p1' #website
    while True:
            try:
                r = requests.get(url_to_type)
                break
            except:
                print("มีปัญหากลับไปรีเควสใหม่")
                print("ที่ลิ้ง: "+str(url_to_type))
                time.sleep(2)
                continue
    soup = BeautifulSoup(r.text, "lxml")
    type_car = soup.select("div.item a")
    for i in type_car:
        print("Type "+i['href'])
        keep_typelink.append('https://chobrod.com'+i['href'])
        if(i['href'] == "/car-evhybrid"):
            break

    for i in keep_typelink:
        link = (i+'/p')
        print(link)
        while True:
            try:
                r = requests.get(i)
                break
            except:
                print("มีปัญหากลับไปรีเควสใหม่")
                print("ที่ลิ้ง: "+str(i))
                time.sleep(3)
                continue
        soup = BeautifulSoup(r.text, "lxml")
        num_car = soup.select("span.lh-40 b") #จำนวนรถทั้งหมด
        for i in num_car: #ลูปหาจำนวนหน้ามากที่สุด
            k = i.text.strip().split(" ")
            k = k[0].replace(",","")
            max_typecar.append(k)
        maxpage = (int(k)//15)+1
        print(maxpage)
        count=maxpage
        num=1
        j=0
        while(num != count):
            print("page "+str(num))
            url_to_num = link+str(num)
            while True:
                try:
                    r = requests.get(url_to_num)
                    break
                except:
                    print("มีปัญหากลับไปรีเควสใหม่")
                    print("ที่ลิ้ง: "+str(url_to_num))
                    time.sleep(8)
                    continue
            soup = BeautifulSoup(r.text,"lxml")
            url_linkcar = soup.select("h2.title-listitem a") #linkของรถแต่ละคัน
            for i in url_linkcar:
                print("link "+str(j+1)+i['href'])
                keep_sendlink.append('https://chobrod.com'+i['href'])
                j+=1
            num+=1
    print("End getLink")

def getSendLink():
    print("Start Chobrod")
    getLink()
    print("Start getSendLink")
    Main(keep_sendlink,max_typecar)
    print("End getSendLink")
    print("End Chobrod")
getSendLink()
