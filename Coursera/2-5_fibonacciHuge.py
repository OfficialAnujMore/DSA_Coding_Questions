# def fibonacci_1(n,m):
#     a = n
#     b = m   
#     # print(a, b, end=" ")
#     if n <=1:
#         return n
#     else:
#         for i in range(2, n+1):
#             c = a + b
#             # print(c, end=" ")
#             a = b
#             b = c

#     return c





# x = list(int,input().split())
# print(fibonacci_1(x[0],x[1]))

import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        print("---- ===0000= ")
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        print("---- ==== ")
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input = sys.stdin.read()
    print("--3333333-- ==== ")
    n, m = map(int, input.split())
    print("-222222222222--- ==== ")
    print(get_fibonacci_huge_naive(n, m))