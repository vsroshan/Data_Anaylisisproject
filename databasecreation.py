#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Creating Database Covid

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="covid"  
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE covid")
mydb.commit()

#Creating Table Users
mycursor.execute("CREATE TABLE users (uname VARCHAR(10), pwd VARCHAR(8))")
mydb.commit()
#inserting Records in to the table Users
sql = "INSERT INTO users (uname, pwd) VALUES (%s, %s)"
val = ("Admin", "admin123")
mycursor.execute(sql,val)
mydb.commit()

