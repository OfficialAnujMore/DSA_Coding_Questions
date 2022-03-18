def fibonacci_1(n):
    a = 0
    b = 1
    # print(a, b, end=" ")
    if n <= 1:
        return n
    else:
        for i in range(2, n+1):
            c = a + b
            # print(c, end=" ")
            a = b
            b = c

    return c % 10


def fibonacci_2(n):

    if n <= 1:
        return n
    else:

        return fibonacci_2(n-1) + fibonacci_2(n-2)


n = int(input())
print(fibonacci_1(n))
# print("----", fibonacci_2(n))
