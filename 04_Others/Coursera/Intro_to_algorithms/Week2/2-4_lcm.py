def gcd(a, b):

    if b == 0:
        return a
    else:

        return gcd(b, a % b)

        # n1 * n2  = LCM * GCD


def lcm(a, b):

    lcm = a*b // gcd(a, b)

    return lcm


x = list(map(int, input().split()))
print(lcm(x[0], x[1]))
