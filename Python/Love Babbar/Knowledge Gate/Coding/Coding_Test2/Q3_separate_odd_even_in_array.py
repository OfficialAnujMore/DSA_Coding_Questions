n = int(input("Enter number of elements in array"))
ele = []
odd = []
eve = []

for i in range(0,n):
    ip = int(input("Enter element at position " + str(i) + ": " ))
    ele.append(ip)


for i in range(0,len(ele)):
    if ele[i]%2==0:
    
        odd.append(ele[i])
    else:
        eve.append(ele[i])
    
print(len(ele))
print(ele)
print(eve)
print(odd)