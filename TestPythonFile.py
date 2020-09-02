#!/usr/bin/python3

import sqlite3

# Complete the function below.
conn = sqlite3.connect('C:\\Users\\Nethrrashri\\Desktop\\Python 3 Programing Handson\\Sample.db')
#conn = sqlite3.connect('SAMPLE.db')
#create connection cursor
cursor = conn.cursor()


  #create table ITEMS using the cursor

sql1 = 'DROP TABLE IF EXISTS ITEMS'

sql2 = '''

       CREATE TABLE ITEMS (

       item_id INT(6) NOT NULL,

       item_name CHAR(20) NOT NULL,

       item_description CHAR(20),

       item_category CHAR(20),

       quantity_in_stock INT(6)

       )

      '''

cursor.execute(sql1)
cursor.execute(sql2)

#commit connection 

conn.commit()

cursor.execute("select * from ITEMS")

rowout=[]     
for row in cursor.fetchall():
    rowout.append(row)
    print( rowout  )  

#close connection 

conn.close()


