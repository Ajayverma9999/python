a=int(input("enter the number"))
b=a
rev=0
while a>0:
          rem=a%10
          rev=rev+(rem*rem*rem)
          a=int(a/10)
print(rev)
if b==rev:
          print("amstong number")
else:
          print(" not amstrong number")
          
