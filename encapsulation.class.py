class person:
    def setage(self,age):
        if age>0 and age<=100:
            self.age=age
        else:
            self.age=0
            print("plz enter a valid age")
                
    def getage(self):
        return self.age


p=person()
p.setage(12)

age=p.getage()
print(age)
