def prime(a):
    c=0
    for x in range(2,a):
        if a%x==0:
            c=1
            break
    if c==0:
        print(a,"is prime")
    else:
        print(a,"is not prime")


prime(10)
prime(17)
        
