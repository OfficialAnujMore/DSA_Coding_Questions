# 5 4 3 2 1 1 2 3 4 5 
# 5 4 3 2 2 3 4 5 
# 5 4 3 3 4 5 
# 5 4 4 5 
# 5 5


n = 6
for i in range(1,n):

    for j in range(n-1,i-1,-1):
        print(j,end=" ")
    
    for j in range(i,n):
        print(j,end=" ")
    print()