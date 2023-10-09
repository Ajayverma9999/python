try:
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    c=a/b
    print(c)
except ValueError as e:
    print (e)
except ZeroDivisionError as e:
    print(e)
print("hello")
