x=10


def one():
    global x
    print(x)
    x=20


def two():
    global x
    print (x)


one()
two()
