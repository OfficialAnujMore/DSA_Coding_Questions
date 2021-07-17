n = int(input("Enter number of elements in array : "))
ele = []
count = {}
for i in range(0,n):
    ip = int(input("Enter element at position "  + str(i) + ": "))
    # ip = int(input("Enter element at position " + str(i) + ": " ))
    ele.append(ip)

print(ele)

for i in range(0,len(ele)):
    if ele[i] in count:
        count[ele[i]]+=1
    else:
        count[ele[i]] = 1

print(count)

for i in count:
    if count[i]>1:
        print("Count of element",ele[i],"is ",count[ele[i]])
