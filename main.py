def fun1(*values):
    """print all value"""
    for value in values:
        print(value)

def calculation(a,b):
    """print sum and minus"""
    return a+b , max(a,b)-min(a,b)

def showEmployee(name, salary=9000):
    """print name and salary"""
    print("Employee {} salary is: {}".format(name,salary))

def outer_fun(a,b):
    def addition_fun(a,b):
        return a+b
    return addition_fun(a,b) +5

def displayStudent(name, age):
    print("{} is {} years old".format(name,age))

showStudent = displayStudent
showStudent("mahdi", 25)

