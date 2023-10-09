class one:
    def show(self):
        print("show from one class")

class temp(one):
    def show(self):
        print("show from temp class")

t=temp()
t.show()
