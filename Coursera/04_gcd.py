def gcd2(a, b):

    if b == 0:
        return a
    else:
        # print(b, a % b)
        return gcd2(b, a % b)


def gcd1(a, b):

    res = 0

    for i in range(2, a+b):
        if a % i == 0 and b % i == 0:
            res = i

    return res


# print(gcd1(10, 30))
print(gcd2(357,234))
