class Person:

    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


class Employee(Person):
    
    def isEmployee(self):
        return True


person = Person('Anuj')
print(person.getName(), person.isEmployee())

emp = Employee('Amit')
print(emp.getName(), emp.isEmployee())