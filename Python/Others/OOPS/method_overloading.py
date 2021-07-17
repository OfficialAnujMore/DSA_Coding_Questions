
# Method overloading is a compile time polymorphsim in which the method has same name but different parameters


def product(a, b,c=None):

    if c==None:
        product = a*b
        return product  
    else:
        product = a*b*c
        return product  
        





print(product(2,3))
print(product(2,3,2))