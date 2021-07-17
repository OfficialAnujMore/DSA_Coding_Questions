# 1
# 3 2
# 6 5 4
# 10 9 8 7

start = 1
stop = 2

num = stop
for i in range(2,6):
    for j in range(start,stop):
        num-=1
        print(num,end=" ")
    print(" ")
    start = stop
    stop += i
    num  = stop

