#   *
#   * *
#  * * *
# * * * *

n = 4
k = n-1

#rows
for i in range(0,n):

    # spaces
    for j in range(0,k):
        print(end=" ")
    k-=1

    for j in range(0,i+1):
        print("* ",end="")
    print("\r")


