# def result(n):
#     a = 0
#     b = 1
#     sum = 1

#     if n <= 1:
#         return n
#     else:
#         for i in range(2, n+1):
#             c = a + b

#             sum += c
#             # print(c, end=" ")
#             a = b
#             b = c

#     return sum % 10


# n = int(input())
# print(result(n))

n = int(input())

if n <= 1:
    print(n)
    quit()


lesser = (n+2) % 60
if lesser == 1:
    print(0)
    quit()
elif lesser == 0:
    print(9)
    quit()


def fibo(n):
    a, b = 0, 1
    for _ in range(2, lesser+1):
        c = a+b
        c = c % 10
        b, a = c, b
    if c != 0:
        print(c-1)
    else:
        print(9)


fibo(lesser)
