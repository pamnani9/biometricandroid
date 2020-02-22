#!C:\Users\Sunny\AppData\Local\Programs\Python\Python36\python.exe
import cgi
import pymysql
import json
from Connection import *


print("Content-Type:text/html\n\n")
data=cgi.FieldStorage()
data=data.getvalue("req")

data=eval(data)

print(data)
name=data["name"]
mobile=data["mob"]
email=data["email"]
branch=data["branch"]



try:
	cursor=conn.cursor()
	query="Insert into sunny(Name,Mobile,Email,Branch)values('"+name+"','"+mobile+"','"+email+"','"+branch+"')"
	cursor.execute(query)
	conn.commit()
	print("Data Saved")

except:
	print("Email already taken")
conn.close()




