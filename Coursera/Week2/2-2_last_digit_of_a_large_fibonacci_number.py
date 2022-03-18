def result(n):
    a = 0
    b = 1

    if n <= 1:
        return n
    else:
        for i in range(2, n+1):
            c = a + b
            c = c % 10
            # print(c, end=" ")
            a = b
            b = c

    return c


n = int(input())
print(result(n))
