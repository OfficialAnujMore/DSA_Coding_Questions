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
print(gcd(42,24))