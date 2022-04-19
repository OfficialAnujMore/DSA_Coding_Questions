'''
a^b
If b in even:
    (a^2)^(b/2)
if b is odd:
    a* (a)^(b-1)

'''


def fastPower(a, b):
    # a^b

    res = 1
    while b:
        if ((b & 1) != 0):  # b % 2
            res = res * a
        a = a*a
        b = b >> 1  # b // 2

    return res


a = 3
b = 5
print(fastPower(a, b))
