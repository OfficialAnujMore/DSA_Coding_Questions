'''
GCD using euclids principle
'''

def gcd(a,b):
    c = 1
    while b!=0:

        c = a % b
        a = b
        b = c
    return a
def gcdUsingRecursion(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)
print(gcd(42,24))
print(gcdUsingRecursion(42,24))