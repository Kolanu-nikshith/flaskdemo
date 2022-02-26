

import pymysql
table_created=1

conn = pymysql.connect(
        #host= "test.cq7sapjb7scv.ap-south-1.rds.amazonaws.com", #endpoint link
        host = "localhost",
        port = 3306, # 3306
        user = "root", # admin
        password = "qwertyuiop", #rds.password, #adminadmin
        db = "test", #test
        )

#Table Creation
if table_created:
    table_created=0
    cursor=conn.cursor()
    lm75 = "lm75"
    mq2 = "mq2"
    mq7 = "mq7"
    create_lm75 = """create table IF NOT EXISTS lm75 (id int NOT NULL AUTO_INCREMENT,value varchar(254), inserttime DATETIME DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));"""
    create_mq2 =  """create table IF NOT EXISTS mq2 (id int NOT NULL AUTO_INCREMENT,value varchar(254), inserttime DATETIME DEFAULT CURRENT_TIMESTAMP,  PRIMARY KEY (id));"""
    create_mq7 =  """create table IF NOT EXISTS mq7 (id int NOT NULL AUTO_INCREMENT,value varchar(254), inserttime DATETIME DEFAULT CURRENT_TIMESTAMP,  PRIMARY KEY (id));"""
    cursor.execute(create_lm75)
    cursor.execute("INSERT INTO lm75 (value) VALUES (%s)", (lm75))

    cursor.execute(create_mq2)
    cursor.execute("INSERT INTO mq2 (value) VALUES (%s)", (mq2))

    cursor.execute(create_mq7)
    cursor.execute("INSERT INTO mq7 (value) VALUES (%s)", (mq7))

    conn.commit()



def get_lm75():
    try:
        cur=conn.cursor()
        cur.execute("SELECT *  FROM lm75")
        details = cur.fetchall()
    except:
        print("fetching lm75 details failed")
        return "failed"
    return details

def get_mq2():
    try:
        cur=conn.cursor()
        cur.execute("SELECT *  FROM mq2")
        details = cur.fetchall()
    except:
        print("fetching mq2 details failed")
        return "failed"
    return details

def get_mq7():
    try:
        cur=conn.cursor()
        cur.execute("SELECT *  FROM mq7")
        details = cur.fetchall()
    except:
        print("fetching mq7 details failed")
        return "failed"
    return details


def insert_lm75():
    lm75 = "lm75"
    try:
        cur=conn.cursor()            
        cur.execute("INSERT INTO lm75 (value) VALUES (%s)", (lm75))
        conn.commit()
    except:
        return "Inserting into lm75 failed"
    return "Inserting into lm75 success"

def insert_mq2():
    mq2 = "mq2"
    try:            
        cur=conn.cursor()
        cur.execute("INSERT INTO mq2 (value) VALUES (%s)", (mq2))
        conn.commit()
    except:
        return "Inserting into mq2 failed"
    return "Inserting into mq2 success"

def insert_mq7():
    mq7 = "mq7"
    try:            
        cur=conn.cursor()
        cur.execute("INSERT INTO mq7 (value) VALUES (%s)", (mq7))
        conn.commit()
    except:
        return "Inserting into mq7 failed"
    return "Inserting into mq7 success"

