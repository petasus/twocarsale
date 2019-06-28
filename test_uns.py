import requests
from bs4 import BeautifulSoup
import datetime

def get_Type(soup): #ประเภทรถ
    detail = soup.select("div.main-tab ul")
    backup=[]
    j=0
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        j+=1
        if(i == "ประเภทรถ"):
            ty = backup[0][j]
            break
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
    detail = soup.select("div.main-tab ul")
    backup=[]
    j=0
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        j+=1
        if(i == "ยี่ห้อ"):
            br = backup[0][j]
            break
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
    detail = soup.select("div.main-tab ul")
    backup=[]
    j=0
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        j+=1
        if(i == "รุ่น"):
            mo = backup[0][j]
            break
        else:
            mo = "-"
    print(mo)
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
    detail = soup.select("div.main-tab ul")
    backup=[]
    j=0
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        j+=1
        if(i == "รุ่นย่อย"):
            sm = backup[0][j]
            break
        else:
            sm = "-"
    print(sm)

def get_Gear(gear,g): #ระบบเกียร์
    a = g-2
    ge = gear[a]
    print(ge)

def get_Web(soup): #ชื่อเว็บ
    we = 'unseencar.com'
    print(we)

def get_Post(soup): #วันที่โพส
    detail = soup.select("div.date")
    backup=[]
    months = ['ม.ค','ก.พ','มี.ค','เม.ย','พ.ค','มิ.ย','ก.ค','ส.ค','ก.ย','ต.ค','พ.ย','ธ.ค']
    for i in detail:
        backup.append(i.text.strip().split(' '))
    dd = backup[0][0]
    mm = backup[0][1]
    yy = backup[0][2].replace(",","")
    for i in months:
        if i == mm:
            mm = str(months.index(i)+1)
            if(int(mm) <= 9 ):
                mm = "0"+ str(mm)
    if(int(dd) <= 9 ):
        dd = "0"+ str(dd)
    po = (yy +'-'+ mm +'-'+dd)
    print(po)

def get_Price(soup): #ราคา
    detail = soup.select("div.price")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    bu = backup[0]
    if(bu == "ติดต่อผู้ขาย"):
        pr = "0"
    else:
        bu1 = bu.replace(",","")
        pr = bu1.replace(" ","")
    print(pr)

def get_Location(soup): #จังหวัด
    detail = soup.select("div.date")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split(' '))
    for i in backup[0]:
        j+=1
        if(j == 4):
            lo = backup[0][3]
            break
        else:
            lo = "-"
    print(lo)

def get_Year(soup): #รุ่นปี
    detail = soup.select("div.main-tab ul")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        j+=1
        if(i == "ปีที่ผลิต"):
            ye = backup[0][j]
            break
        else:
            ye = "-"
    print(ye)

def get_Mile(soup): #เลขไมล์ที่ใช้ไป หน่วยเป็น(กม.)
    detail = soup.select("div.main-tab ul")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        j+=1
        if(i == "เลขไมล"):
            bu = backup[0][j].replace("km","")
            bu1 = bu.replace(",","")
            mi = bu1.replace(" ","")
            break
        else:
            mi = "-"
    print(mi)

def get_Color(soup): #สีรถ
    detail = soup.select("div.main-tab ul")
    j=0
    backup=[]
    for i in detail:
        backup.append(i.text.strip().split('\n'))
    for i in backup[0]:
        j+=1
        if(i == "สี"):
            co = backup[0][j]
            break
        else:
            co = "-"
    print(co)

def get_Seller(soup): #ชื่อผู้ขาย
    detail = soup.select("span.name-cat")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    if(backup == []):
        se = "-"
    else:
        se = backup[0]
    print(se)

def get_Tel(soup): #เบอร์ผู้ขาย
    detail = soup.select("span.span-hotline")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    if(backup == []):
        te = "-"
    else:
        bu = backup[0].replace(" ","")
        te = bu[0:10].replace(",","")
    print(te)

def get_Place(soup): #ที่อยู่
    detail = soup.select("div.maps-detail")# span.map-content
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    #pl = backup[0]
    pl = "-"
    print(pl)

def get_description(soup): #รายละเอียด
    detail = soup.select("div.list-news-home")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    de = backup[0]
    print(de)
    #if(backup[2] == []): #option
    #    op = "ไม่มีข้อมูล"
    #else:
    #    op = backup[3]

def get_specification(soup): #ข้อมูลจำเพาะทางเทคนิค
    detail = soup.select("ul.list-ts")
    backup=[]
    for i in detail:
        backup.append(i.text.strip())
    #print(backup)
    #if(backup == []):
    #    sp = "ไม่มีข้อมูล"
    #else:
    #    sp = backup[0]
    sp = "-"
    print(sp)

def get_Image(soup):
    detail = soup.select("div.thumb img.cursor-p")
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

def Main(links,gears):
    j=1
    for i in links:
        print("link no." + str(j) + " " + i)
        r = requests.get(i)
        soup = BeautifulSoup(r.text, "lxml")
        j+=1
        CarDetail = {}
        #CarDetail['typ'] = get_Type(soup)###
        #CarDetail['bra'] = get_Brand(soup)###
        #CarDetail['mod'] = get_Model(soup)###
        #CarDetail['sub'] = get_Submodel(soup)###
        #CarDetail['gea'] = get_Gear(gears,j)###
        CarDetail['web'] = get_Web(soup)
        CarDetail['pos'] = get_Post(soup)
        CarDetail['pri'] = get_Price(soup)
        CarDetail['loc'] = get_Location(soup)
        CarDetail['yea'] = get_Year(soup)
        CarDetail['mil'] = get_Mile(soup)
        CarDetail['col'] = get_Color(soup)
        CarDetail['sel'] = get_Seller(soup)
        CarDetail['tel'] = get_Tel(soup)
        CarDetail['pla'] = get_Place(soup) #มีข้อมูลแต่เก็บไม่ได้ มันhidden
        CarDetail['des'] = get_description(soup)
        ###CarDetail['cla'] = get_description(soup)#อุบัติเหตุ ชน น้ำท่วม แต่ง ติดแก๊ส
        ###CarDetail['pro'] = get_description(soup)#โปรโมชั่น ส่วนลด ดาวน์
        ###CarDetail['ser'] = get_description(soup)#รับประกันหลังการขาย
        CarDetail['spe'] = get_specification(soup) #มีข้อมูลไม่ทุกอันแต่เก็บไม่ได้ มันhidden
        CarDetail['img'] = get_Image(soup)
        #CarDetail['dup'] = get_duplicate(soup) #check ซ้ำ
        #CarDetail['upd'] = get_update(soup) #updatedatabase

def gLink():
    num = 1
    count = 3
    ksl=[]
    j=0
    gea=[]
    backup=[]
    a=0
    b=0
    while(num != count):
        url_num = 'https://unseencar.com/taladrod/p'+str(num)+''
        r = requests.get(url_num)
        soup = BeautifulSoup(r.text,"lxml")
        url_linkcar = soup.select("h3.title-20 a") #linkของรถแต่ละคัน
        for i in url_linkcar:
            print("link "+str(j+1)+i['href'])
            ksl.append('https://unseencar.com'+i['href'])
            j+=1
        car_gea = soup.select("div.display-ib span.span-hotline")
        for i in car_gea:
            backup.append(i.text.strip())
            a+=1
        if(a==0):
            gea = "-"
        else:
            while(b != a):
                if(backup[b]=="เกียร์ธรรมดา" or backup[b]=="เกียร์อัตโนมัติ" ):
                    gea.append(backup[b])
                b+=1
        num+=1
    Main(ksl,gea)
gLink()
