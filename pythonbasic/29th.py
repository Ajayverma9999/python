n=int(input("enter the number"))
c=0
for x in range(2,n):
    if n%x==0:
        c=1
if c==0:
    print(n," is prime number")
else:
    print(n,"is not prime number")
