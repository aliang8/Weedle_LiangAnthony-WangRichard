import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

f1 = open("peeps.csv")

d1 = csv.DictReader(f1)

q = "CREATE TABLE students (name TEXT, id INTEGER)"

c.execute(q)    #run SQL query

for key in d1:
    q = "INSERT INTO students VALUES ('" + key['name'] + "'," + key['id'] + ")"
    c.execute(q)


f2 = open("courses.csv")

d2 = csv.DictReader(f2)

q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"

c.execute(q)

for key in d2:
    q = "INSERT INTO courses VALUES ('" + key['code'] + "'," + key['id'] + "," + key['mark'] + ")"
    c.execute(q)


#==========================================================
db.commit() #save changes
db.close()  #close database


