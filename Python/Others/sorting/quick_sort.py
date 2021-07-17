def swap(a,i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def partition(a, l, r):
    pivot = a[r]
    i = l-1
    for j in range(l,r):
        if a[j] <=pivot:
            i+=1
            swap(a,i,j)
    swap(a,i+1,r)
    return i+1

def quick_sort(a, l, r):

    if len(a)<1:
        return a
    if l<r: 
        p = partition(a, l, r)
        quick_sort(a, l, p-1)
        quick_sort(a, p+1, r)
    return a
arr = list(map(int,input().split()))
n = len(arr)
print(quick_sort(arr,0,n-1))

# Worst Case Time Complexity [ Big-O ]: O(n2)
# Best Case Time Complexity [Big-omega]: O(n*log n)
# Average Time Complexity [Big-theta]: O(n*log n)

