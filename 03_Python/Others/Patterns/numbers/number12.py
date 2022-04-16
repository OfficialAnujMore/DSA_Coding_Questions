# 10 
# 10 8 
# 10 8 6 
# 10 8 6 4 
# 10 8 6 4 2


n = 5
num = 2*n 
evenNum  = num
for i in range(1,n+1):
    evenNum = num
    for j in range(i):
        print(evenNum,end=" ")
        evenNum-=2
    print()