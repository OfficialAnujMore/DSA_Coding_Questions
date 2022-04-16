
# 1 
# 2 3 4 
# 5 6 7 8 9

n =3
s = 2
num = 1

for i in range(0,n):
    for j in range(1,s):
        print(num,end=" ")
        num+=1
    s +=2
    print("\r")