class ageException(Exception):
    def __init__(self):
        print("age is below 18")
age =int(input("enter the number"))
try:
    if age <18:
        raise ageException
    else:
        print("you are eligible to cast vote")
except ageException as e:
    print(e)
