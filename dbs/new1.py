# import sqlite3
# try:
#     con=sqlite3.connect(r'C:\Users\Dell\Desktop\abc.db')
#     print("connection successfull")
# except:
#     print("not connet databae")

# step1

# import sqlite3
# try:
#     con=sqlite3.connect('abc.db')
#     print("connection successfull")
# except:
#     print("not connet databae")

# step2


# create table 

# import sqlite3
# con=sqlite3.connect('abc.db')
# print("data base are connected")

# # create table
# con.execute('''CREATE TABLE emp
# (ID INT PRIMARY KEY NOT NULL,
# NAME TEXT NOT NULL,
# AGE INT NOT NULL)
# ''')
# print("table are created ")
# con.close


# step3

# import sqlite3
# con=sqlite3.connect('abc.db')
# print("data base are connected")
 
# # create table
# con.execute('''INSERT INTO emp(ID,NAME,AGE)VALUES(101,"HARRY",21)''')
# con.commit()

# print("ADD DATA INTO TABLE ")
# con.close


import sqlite3
con=sqlite3.connect('abc.db')
print("data base are connected")
  
# create table
a=con.execute('''select * from emp''')
for row in a:
    print ("ID = ",row[0])
    print ('NAME = ',row[1])
    print ('AGE = ',row[2])

con.close