for b in range(1,1001):
    a=b
    rev=0
    while a>0:
        rem=a%10
        rev=rev+(rem*rem*rem)
        a=int(a/10)
    if b==rev:
        print(b,"amstrong number")
