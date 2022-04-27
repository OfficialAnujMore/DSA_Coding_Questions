'''
Find numbers in range that are divisible by a or b.
Example 5 and 7
'''

def inRange(n,a,b):
    c1 = n//a
    c2 = n//b
    c3 = n//(a*b)
    return c1+c2-c3

print(inRange(100,5,7))