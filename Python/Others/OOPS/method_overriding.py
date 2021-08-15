# Method overridding is 
# run time polymorphism 
# in which the method name 
# and parameter list is same
class Parent:

    def identity(self):
        print("Parent class")

    def age(self,age):
        self.age = 40
        print("Parents age is " +str(age))

class Child(Parent):

    def identity(self):
        print("Child class")

    # def age(self,age):
    #     self.age = 20
    #     print("Childs age is " + str(age))
p = Parent()
p.identity()
p.age(50)

c = Child()
c.identity()
c.age(20)