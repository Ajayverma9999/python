import pymysql

try:
    con=pymysql.connect(host="localhost",user="root",password="root",db="pydb")
    cursor=con.cursor()
    cursor.execute("create table student(name varchar(20) not null,roll int(3)not null primary key)")
    print("table created successfully")
    con.commit()

except Exception as e:
    con.rollback()
    print(e)

con.close()
