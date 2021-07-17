# Wapp to reverse a array


def reverse_array(n):
    arr = []
    for i in range(0,n):
        ele = int(input("Enter element in array:"))
        arr.append(ele)

    print("The array of length",n, "is" ,arr)

    # start,end = 0,len(arr)-1
    
    # while start < end:

    #     temp = arr[start]
    #     arr[start] = arr[end]
    #     arr[end] = temp
        
    #     start+=1
    #     end-=1
        
    # return arr

    for i in range(0,n//2):
        arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    print(arr)

n = int(input("Enter length of array"))
print(reverse_array(n))

