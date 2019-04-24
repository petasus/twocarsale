#! /usr/bin/env python3.5
# -*- coding: utf-8 -*-
import pymysql

def conDB():
    try:
        db = pymysql.connect(host='localhost', user='root', passwd='123456789', db='usedcarsproject',charset='utf8',use_unicode=True)
        return db
    except :
        print("connect error")
