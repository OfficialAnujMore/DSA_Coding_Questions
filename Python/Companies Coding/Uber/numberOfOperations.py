def operations(arr, n):

    i = 1
    count = 0
    while i < n-1:
        a = arr[i] != arr[i-1]+1
        b = arr[i] != arr[i-1]-1
        c = arr[i] != arr[i-1]+2
        d = arr[i] != arr[i-1]-2

        print(a,b,c,d)
        if (arr[i] != arr[i-1]+1) or (arr[i] != arr[i-1]-1) or (arr[i] != arr[i-1]+2) or (arr[i] != arr[i-1]-2):
            arr[i] = arr[i-1]+1
            count+=1
        i+=1
    return arr,count



arr = [6, 4, 1, 7, 10]
print(operations(arr, len(arr)))
