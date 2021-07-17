def Linear_search(n,size,a):

    for i in range(size):
        if a[i] == n:
            return "Position of element",n,"is at",i+1


size  = int(input("Enter size of array :"))
a = []
for i in range(size):
    ele = int(input("Enter elemenet in array: "))
    a.append(ele)
print(a)
n = int(input("Enter element find in given array :"))

print(Linear_search(n,size,a))