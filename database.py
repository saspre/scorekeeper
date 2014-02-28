#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
import config

#drop and create tables
def initDatabase():
    #read config file
    database = config.configSectionMap("database")['name']
    con = None

    f = open('schema.sql', 'r')
    sql = f.read()
    conn = lite.connect(database)
    cur = conn.cursor()
    cur.executescript(sql)
    conn.commit()
    conn.close()
