#! /usr/bin/env python3.5
# -*- coding: utf-8 -*-
ThisFileDetail="""
ีuploadData.py เอาไว้ใช้อัพโหลดข้อมูลขึ้น database
Ver 1.0
by Sorapunya Insala
"""

import connect
def uploadToSql(CarDetail):
    db=connect.conDB()
    c = db.cursor()
    for i in CarDetail:
        print(i)
        try:
            c.execute("SET NAMES utf8mb4;")
            sql = """INSERT INTO main_data (`mod_id`, `color`, `price`, `years`, `mile`, `seller`, `tel`, `loc`, `date`, `img_name`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            #เช็คข้อมูลซ้ำ
            CKsql = """SELECT * FROM main_data WHERE `mod_id`=%s AND `color`=%s AND `price`=%s AND `years`=%s AND `mile`=%s AND `seller`=%s"""
            CKExis = c.execute(CKsql,(i["""mod"""],i["""col"""],i["""pri"""],i["""yea"""],i["""mil"""],i["""sel"""],))
            print(1)
            if CKExis:
                print("Duplicate Data in List..")
            else:
                print(27)
                c.execute(sql, (i["""mod"""],i["""col"""],i["""pri"""],i["""yea"""],i["""mil"""],i["""sel"""],i["""tel"""],i["""loc"""],i["""dat"""],i["""img"""]))
                db.commit()

        except Exception as e:
            print("ข้อมูลมีปัญหา")
            db.rollback()
            print(e)
    if c:
        c.close()
    print("------------------")
    print("------------------")
    print("------------------")
