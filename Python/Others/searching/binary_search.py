def binary_search(arr, n):

    s, e = 0, len(nums) - 1
    while (s<=e):
        mid = (s+e)//2

        if (arr[mid]==n):
            return mid
        elif (arr[mid]>n):
            e = mid-1
        else:
            s = mid + 1      
    return -1

arr = list(map(int, input().split()))
n = int(input())
print(binary_search(arr,n))
'''
Time complexity
1st time n
2nd time n/2
3rd time n/2/2 ==> n/2**2
kth time n/2/k ==> n/2**k
Therefore timecomplexity is log2(n)
'''
# --------------------

'''
space complexity: O(1)
'''
