#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('webstore.db')

conn.execute("INSERT INTO user (name,email,phone,pwd,role) \
      VALUES ('Allen', 'yaseen@gmail.com', '09454208024','abc','admin' )")

conn.commit()

print ("Values inserted")
conn.close()
print ("Opened database successfully")

# conn.execute('''CREATE TABLE user
#          (
#          name           TEXT    NOT NULL,
#          age             INT,
#          role            TEXT,
#          email           TEXT,
#          phone           TEXT ,
#          card           TEXT,
#          pwd            TEXT
#          );''')
# print ("Table created successfully")
# conn.close()