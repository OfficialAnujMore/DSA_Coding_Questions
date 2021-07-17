def insertion_sort(a):
    
    for i in range(1,len(a)):
        current = a[i]
        j = i-1
        while(a[j]>current and j>=0):
            a[j+1] = a[j]
            j-=1
        a[j+1] = current
    return a

arr = list(map(int, input().split()))
print(insertion_sort(arr))
'''
Time complexity 
Best = O(n)
Average, Worst = O(n**2)


'''