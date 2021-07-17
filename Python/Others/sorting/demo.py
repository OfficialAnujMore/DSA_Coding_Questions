def rotation(a,n,k):

    # x = k % n

    for i in range(0,k+1):
        first = a[0]
        for j in range(0,n-1):
            a[j] = a[j+1]
        a[n-1] = first

    # for t in range(0,k):
    # for i in range(0,x+1):
    #     first = a.pop(0)
    #     a.insert(len(a),first)

    for i in range(0,n):
        print(a[i],end=" ")

t = int(input())
n, k = map(int,input().split())
arr = list(map(int,input().split()))
rotation(arr,n,k)