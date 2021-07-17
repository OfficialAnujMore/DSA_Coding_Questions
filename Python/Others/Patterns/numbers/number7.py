# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1

n = 5 
num  = 1

for i in range(1,n):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\r")