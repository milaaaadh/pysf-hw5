def fun1(*values):
    """print all value"""
    for value in values:
        print(value)

def calculation(a,b):
    """print sum and minus"""
    return a+b , max(a,b)-min(a,b)

def showEmployee(name, salary=9000):
    print("Employee {} salary is: {}".format(name,salary))

def displayStudent(name, age):
    print("{} is {} years old".format(name,age))

showStudent = displayStudent
showStudent("mahdi", 25)

