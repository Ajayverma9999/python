x="123"
y=x.isdigit()
print(y)

x="5\u00b2"
y=x.isdigit()
print(x,y)

x="123abc"
y=x.isdigit()
print(y)
