class student:
    schoolname="govt sr sec school"
    city="hisar"
    def __init__ (self,roll,name):
        self.roll=roll
        self.name=name

    def show(self):
        print(self.roll,self.name,student.schoolname,student.city)

    @staticmethod
    def add(a,b):
        c=a+b
        print(c)

student.add(10,20)
