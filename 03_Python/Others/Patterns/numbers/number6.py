# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9


n = 6
num = 0

for i in range(0,n):
    
    for j in range(1,i+1):
        print(num-1,end=" ")
    num+=2
    print("\r")