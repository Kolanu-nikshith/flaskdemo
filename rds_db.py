# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:34:18 2020

@author: hp
"""



import pymysql
import aws_credentials as rds

table_created=1

conn = pymysql.connect(
        host= "zigbeedb.cq7sapjb7scv.ap-south-1.rds.amazonaws.com", #endpoint link
        port = 3306, # 3306
        user = "admin", # admin
        password = "qwertyuiop" #rds.password, #adminadmin
        db = "zigbeedb", #test
        )

#Table Creation
if table_created:
    table_created=0
    cursor=conn.cursor()
    create_table = """create table Details (lm75 varchar(1024))"""
    cursor.execute(create_table)


def insert_details(name,email,comment,gender):
    cur=conn.cursor()
    cur.execute("INSERT INTO Details (lm75)) VALUES (%s)", (lm75))
    conn.commit()

def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Details")
    details = cur.fetchall()
    return details
