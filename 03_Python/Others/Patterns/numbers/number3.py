# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5


n = 5
num = 0

for i in range(n,0,-1):
    num+=1
    for j in range(1,i+1):
        print(num,end=" ")
        
    print("\r")