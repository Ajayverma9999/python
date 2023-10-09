class student:
    def __init__(self,n,r):
        self.name=n
        self.roll=r

    def display(self):
        print(self.name,self.roll)

s=student("ram",1)
s.display()

s2=student("shyam",2)
s2.display()

