import requests
from bs4 import BeautifulSoup
import datetime

def get_Type(soup): #ประเภทรถ
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "ประเภทรถ"):
            k = j+1
        j=j+1
    if(k != 1000):
        ty = backup[k]
        if(ty == "ยี่ห้อ"):
            ty = "-"
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
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "ยี่ห้อ" ):
            k = j+1
        j=j+1
    if(k != j):
        br = (backup[k].lower())
        if(br == "BUGATTI"):
            br = "Bugatti"
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
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "รุ่น" ):
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
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "รุ่นย่อย" ):
            k = j+1
        j=j+1
    if(k != 1000):
        sm = (backup[k].lower())
    else:
        sm = "-"
    print(sm)

def get_Gear(soup): #ระบบเกียร์
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "ระบบส่งกำลัง" ):
            k = j+1
        j=j+1
    if(k != 1000):
        ge = backup[k]
    else:
        ge = "-"
    print(ge)

def get_Web(soup): #ชื่อเว็บ
    we = 'rodmuesong.com'
    print(we)

def get_Post(soup): #วันที่โพส
    detail = soup.select("div.title-page p.info-title")
    backup=[]
    months = ['ม.ค','ก.พ','มี.ค','เม.ย','พ.ค','มิ.ย','ก.ค','ส.ค','ก.ย','ต.ค','พ.ย','ธ.ค']
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0].split(" ")
    dd = bu[2]
    mm = bu[3]
    yy = bu[4]
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
    detail = soup.select("div.left-content p.price")
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
    detail = soup.select("div.title-page p.info-title")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0].split(" ")
    lo = bu[0]
    print(lo)

def get_Year(soup): #รุ่นปี
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "ปีที่ผลิต" ):
            k = j+1
        j=j+1
    if(k != 1000):
        ye = backup[k]
    else:
        ye = "-"
    print(ye)

def get_Mile(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "เลขไมล์" ):
            k = j+1
        j=j+1
    if(k != 1000):
        mi = backup[k].replace(",","")
    else:
        mi = "-"
    print(mi)

def get_Color(soup): #สีรถ
    detail = soup.select("div.content-col div.item-row span")
    j=0
    k=1000
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    for i in backup:
        if(i == "สี" ):
            k = j+1
        j=j+1
    if(k != 1000):
        co = backup[k]
    else:
        co = "-"
    print(co)

def get_Seller(soup): #ชื่อผู้ขาย
    detail = soup.select("div.col-box h4")
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
    detail = soup.select("div.col-box span")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    te = backup[0].replace(".","")
    print(te)

def get_Place(soup): #ที่อยุ่
    detail = soup.select("div.col-box p")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    pl = backup[0]
    if(pl[0] == "0"):
        pl = "-"
    print(pl)

def get_description(soup): #รายละเอียด
    detail = soup.select("div.description p")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    de = backup[0]
    print(de)

def get_specification(soup): #ข้อมูลจำเพาะทางเทคนิค
    detail = soup.select("div.box-border")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    if(backup == []):
        sp = "ไม่มีข้อมูล"
    else:
        sp = backup[0]
    print(sp)

def get_Image(soup):
    detail = soup.select("a.imageGallery img")
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

def Main(links):
    j=1
    for i in links:
        print("link no." + str(j) + " " + i)
        r = requests.get(i)
        soup = BeautifulSoup(r.text, "lxml")
        j+=1
        CarDetail = {}
        CarDetail['typ'] = get_Type(soup)###
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
        #CarDetail['spe'] = get_specification(soup)
        #CarDetail['img'] = get_Image(soup)
        #CarDetail['dup'] = get_duplicate(soup) #check ซ้ำ
        #CarDetail['upd'] = get_update(soup) #updatedatabase

def gLink():
    ksl=[]
    j=0
    url_num = 'https://rodmuesong.com/รถสำหรับขาย/p1'
    r = requests.get(url_num)
    soup = BeautifulSoup(r.text,"lxml")
    url_linkcar = soup.select("div.content-page div.row div.thumb-img a") #linkของรถแต่ละคัน
    for i in url_linkcar:
        print("link "+str(j+1)+i['href'])
        ksl.append('https://rodmuesong.com'+i['href'])
        j+=1
    Main(ksl)
gLink()
