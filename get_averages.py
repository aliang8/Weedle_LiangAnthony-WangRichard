import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

d = {}
q = "SELECT name, students.id, mark FROM courses, students WHERE students.id = courses.id;"
results = c.execute(q)   
for row in results:
    name = row[0]
    d[name] = [0,0,0]
results = c.execute(q)
for rows in results:
    name = rows[0]
    id = rows[1]
    grade = rows[2]
    d[name][0] += grade
    d[name][1] = id
    d[name][2] += 1
for key in d:
    print "Name: "+ key + " ID: " + str(d[key][1]) + " Average: " + str(float(d[key][0])/d[key][2]) 


#==========================================================
db.commit() #save changes
db.close()  #close database

