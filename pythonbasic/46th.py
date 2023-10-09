a=int(input("enter the number"))
rev=0
while a>0:
    rem=a%10
    rev=(rev*10)+rem
    a=int(a/10)
print(rev)
