y=int(input("enter thr year"))
if (y%4==0 and (y%100!=0 or y%400==0)):
      print("leap year")
else:
    print("not a leap year")
 1990