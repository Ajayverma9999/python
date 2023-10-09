import pymysql
try:
    db=pymysql.connect(host="localhost",user="root",password="root",db="pydb")
    cursor=db.cursor()
    sql="insert into student(name,roll)value(%s,%s)"
    name=input("enter the name")
    roll=int(input("enterb the roll"))
    x=(name,roll)
    cursor.execute(sql,x)
    db.commit()
except Exception as e:
    db.rollback()
    print(e)
print(cursor.rowcount,"record inserted successfully")
db.close()
