def profitMax(n,a):

    a1  = []
    for i in a:
        a1.append(i)

    ans = 0

    for i in range(1,n):
        for j in range(0,i):
            if a[i]%a[j]==0:
                a1[i] = max(a1[i],a[i]+a[j])
        
    for i in range(0,n):
        ans = max(ans,a1[i])
    return ans




  


a = []
n = 0
print(profitMax(n,a))