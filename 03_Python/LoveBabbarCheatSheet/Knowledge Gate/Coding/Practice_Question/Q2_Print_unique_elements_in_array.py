
# Wapp to print unique elements in array


def unique(n):
    
    arr = []
    unique_arr = []
    count = 0
    for i in range(0,n):
        ele = int(input("Enter element in array"))
        arr.append(ele)

    for ele in range(0,len(arr)):
        for traversal in range(0,len(arr)):
            if ele!=traversal:
                if arr[ele] == arr[traversal]:
                    count +=1

        if count == 0:
            unique_arr.append(arr[ele])
    return unique_arr
n = int(input("Enter length of array"))
print(unique(n))

