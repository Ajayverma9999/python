
from abc import ABC,abstractmethod
class polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass

class triangle(polygon):
    def noofsides(self):
        print("i have 3 sides")

class pentagon(polygon):
    def noofsides(self):
        print("i have 5 sides")

class hexagon(polygon):
    def noofsides(self):
        print("i have 6 sides")

class hexagon(polygon):
    def noofsides(self):
        print("i have 6 sides")



 
 
R=triangle()
R.noofsides()

R=pentagon()
R.noofsides()


R=hexagon()
R.noofsides()
