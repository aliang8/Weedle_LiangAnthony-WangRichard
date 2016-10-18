import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

q = "SELECT name, students.id, mark FROM courses, students WHERE students.id = courses.id;"
c.execute(q)   
results = c.fetchall()
d = {};
for row in results:
    
    

#==========================================================
db.commit() #save changes
db.close()  #close database


