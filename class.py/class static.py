class student:
    schoolname="govt sr sec school"
    city="hisar"
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
    def show(self):
        print(self.roll,self.name,student.schoolname,student.city)

s=student(1,"ram")
s.show()
t=student(2,"syam")
t.show()
