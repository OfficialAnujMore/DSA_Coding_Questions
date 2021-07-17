
import math
n,x,k = map(int,input().split(' '))
s =input()
l = math.ceil(n/x)
a = [sorted(list(set([s[j] for j in  range(i*x,min((i+1)*x,n))])))for i in range(l)]
ans = []
k-=1
for lis in a[::-1]:
    ans.insert(0,lis[(k)%len(lis)])
    k = k//len(lis)
print("".join(ans))
