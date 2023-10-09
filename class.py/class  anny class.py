class one:
    def add(self,a,b):
        c=a+b
        print(c)
class two:
    def sub(self,a,b):
        c=a-b
        print(c)

class temp (one,two):
    def mul(self,a,b):
        c=a*b
        print(c)

t=temp()
t.add(10,20)
t.sub(20,5)
t.mul(12,5)
