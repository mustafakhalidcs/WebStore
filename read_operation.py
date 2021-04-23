#!/usr/bin/python

import sqlite3

conn = sqlite3.connect("webstore.db")
cursor = conn.execute("SELECT name, email,pwd,role from user")
for row in cursor:
    print("Name = ", row[0])
    print("Email = ", row[1])
    print("pwd = ", row[2])
    print("role = ", row[3])

    print("*" * 50)


print("Operation done successfully")
conn.close()
