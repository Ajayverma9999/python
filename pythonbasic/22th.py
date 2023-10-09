p=int (input("enter the pin"))
pin=2468
blance=45000
if p==pin:
    a=int(input("enter the amaunt"))

    if a<=blance:
        blance=blance-a
        print(blance,"is your remaing account blance")

    else:
        print("insufficient blance in your account")

else:
    print("invalid pin")
