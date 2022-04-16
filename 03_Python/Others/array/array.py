def rotation(a,n,k):

    for i in range(0,k+1):
        first = a[0]
        for j in range(0,n-1):
            a[j] = a[j+1]
        a[n-1] = first

    for i in range(0,k+1):
        first = a.pop(0)
        a.insert(len(a),first)

    for i in range(0,n):
        print(a[i],end=" ")
    # return a[k+1:]+a[:k+1]

# t = int(input())
# n, k = map(int,input().split())
arr = [1,2,3,4,5,6,7]
n = len(arr)
k = 3
rotation(arr,n,k)