def selection(arr):

    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if (arr[j]<arr[i]):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp


    return arr

arr = list(map(int,input().split()))


print(selection(arr))


'''
Time complexity
O(n**2)
'''