import mysql.connector  

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="#atharvad@322",
    database="demo"
)
cursor=conn.cursor()
cursor.execute('''
    create table if not exists demo(
               id int primary key,
               name varchar(20))
''')
conn.commit()   