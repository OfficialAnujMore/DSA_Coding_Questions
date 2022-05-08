# Only using recursion

def sumOfN(n):
    if n == 1:
        return 1
    return n + sumOfN(n-1)

def powerOf(a,b):
    if b == 0:
        return 1

    return a * powerOf(a, b-1)
print(sumOfN(5))
print(powerOf(4,2))