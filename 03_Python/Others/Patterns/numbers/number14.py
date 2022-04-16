#            1 
#          1 2 
#       1 2 3 
#    1 2 3 4 
#  1 2 3 4 5


n = 5
k = 2*n-2

for i in range(1,n+1):
    num = 1
    for j in range(0,k):
        print(end=" ")
    k = k-2
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()


# n  = 5
# k = 2*n-2


# for i in range(1,n+1):
#     for j in range(0,k):
#         print(end=" ")
#     k = k-2
#     for j in range(0,i):
#         print("*",end = " ")
#     print()


