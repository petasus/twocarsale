#! /usr/bin/env python3.5
# -*- coding: utf-8 -*-
ThisFileDetail="""
ีuploadData.py เอาไว้ใช้อัพโหลดข้อมูลขึ้น database
Ver 1.0
by Sorapunya Insala
"""

from connect import conDB as database

def uploadToSql(CarDetail):
    c = database.cursor()
    for i in CarDetail:
        try:
            c.execute("SET NAMES utf8mb4;")
            sql = """INSERT INTO main_data (`mod_+id`, `color`, `price`, `years`, `mile`, `seller`, `tel`, `loc`, `date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            #เช็คข้อมูลซ้ำ
            CKsql = """SELECT * FROM main_data WHERE `mod_id`=%s AND `color`=%s AND `price`=%s AND `years`=%s AND `mile`=%s AND `seller`=%s"""
            CKExis = c.execute(CKsql,(i["""mod"""],i["""col"""],i["""pri"""],i["""yea"""],i["""mil"""],i["""nam"""],))
            if CKExis:
                print("Duplicate Data in List..")
            else:
                c.execute(sql, (i["""mod"""],i["""col"""],i["""pri"""],i["""yea"""],i["""mil"""],i["""nam"""],i["""tel"""],i["""loc"""],i["""dat"""]))
                database.commit()

        except Exception as e:
            print("ลำดับข้อมูลอันที่ "+str(i['index'])+"มีปัญหา")
            database.rollback()
            print(e)
    if c:
        c.close()
    print("------------------")
    print("------------------")
    print("------------------")
