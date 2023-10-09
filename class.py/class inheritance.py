class person:
    city="hisar"
    state="haryana"

class student(person):
    name="ram"
    roll=1

s=student()
print(s.roll,s.name,s.city,s.state)
