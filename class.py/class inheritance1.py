class person:
    city="hisar"
    state="haryana"

    def add(self,a,b):
     c=a+b
     print(c)

class student(person):
    name="ram"
    roll=1




s=student()
print(s.roll,s.name,s.city,s.state)
s.add(10,20) 

