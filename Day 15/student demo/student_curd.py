import sqlite3

conn=sqlite3.connect("student.db")
cursor=conn.cursor()

cursor.execute('''
    create table if not exists stud(
               sid integer primary key,
               name text not null,
               age integer null)
               ''')
print("Table created")

#cursor.execute("insert into stud(sid,name,age) values(?,?,?)",(1,"Atharva",18))
# print("Row inserted")
# sid=int(input("Enter your id:"))
# sname=input("Enter your name:")
# age=int(input("Enter your age:"))
# cursor.execute("insert into stud(sid,name,age) values(?,?,?)",(sid,sname,age))
# conn.commit()

cursor.execute("Select * from stud")
rows=cursor.fetchall()
print("All rows in table:")
for i in rows:
    print(f"{i[0]}__{i[1]}__{i[2]}")

sid=int(input("Enter your id:"))
cursor.execute("select * from stud where sid=?",(sid,))
row=cursor.fetchone()
print(row)

# cursor.execute("delete from stud where sid=?",(1,))

# cursor.execute("Select * from stud")
# rows=cursor.fetchall()
# print("All rows in table:")
# for i in rows:
#     print(f"{i[0]}__{i[1]}__{i[2]}")

# conn.commit()
# cursor.execute("insert into stud(sid,name,age) values(?,?,?)",(1,"Atharva",18))
# conn.commit()
# sid=int(input("Enter your id:"))
# cursor.execute("select * from stud where sid=?",(sid,))
# newname=input("Enter new name:")
# cursor.execute("update stud set name=? where sid=?",(newname,sid))
# conn.commit()

# cursor.execute("insert into stud(sid,name,age) values(?,?,?)",(3,"Chiku",12))
# cursor.execute("insert into stud(sid,name,age) values(?,?,?)",(4,"om",23))
# conn.commit()

cursor.execute("select * from stud where age between 18 and 25")
row=cursor.fetchall()
print("Name of students having age between 18 and 25 are:")
for i in row:
    print(i[1])

