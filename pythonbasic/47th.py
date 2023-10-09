a=int(input("enter the number"))
b=a
rev=0
while a>0:
    rem=a%10
    rev=(rev*10)+rem
    a=int(a/10)
print(rev)
if b==rev:
    print(b,"palinderome number")
else:
    print(b,"not palinderome number")
