class person:
    def __init__(self,name,city):
        self.name=name
        self.city=city


class student(person):
    def __init__(self,roll,name,city):
        super().__init__(name,city)
        self.roll=roll
    def display(self):
            print(self.roll,self.name,self.city)

class teacher(person):
    def __init__(self,name,city,salary):
        super().__init__(name,city)
        self.salary=salary
    def display(self):
            print(self.name,self.city,self.salary)
              
s=student(1,"ram","hisar")
s.display()

t=student(2,"ajay","hisar")
t.display()

u=teacher("amit","hisar","56000")
u.display()
