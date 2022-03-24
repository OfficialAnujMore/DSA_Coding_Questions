def inversion(a):
    count = 0
    for i in range(0,len(a)+1):
        for j in range(0,len(a)+1):
            # while (i<=len(a) and j<=len(b)):
            if (a[i][j]>a[i+1][j+1]):
                count+=1
        print()


x = int(input())
m = int(input())

a = []
b = []

for i in range(0,m):
    x = list(map(int,input().split()))
    a.append(x)

n = int(input())
for j in range(0,n):
    x = list(map(int,input().split()))
    b.append(x)

inversion(a)
print(a)
print(b)
