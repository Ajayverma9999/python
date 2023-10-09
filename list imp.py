a=[]
n=int(input("enter the number "))
for x in range(0,n):
    name=input("enter the name")
    salary=int(input("enter the salary"))
    emp=[name,salary]
    a.append(emp)
for x in range (0,n):
    for y in range (0,2):
        print(a[x][y],end="")
    print(" ")
