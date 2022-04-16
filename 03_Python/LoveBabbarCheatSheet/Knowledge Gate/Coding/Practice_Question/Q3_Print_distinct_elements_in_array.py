# Wapp to print distinct elements in array

def distinct(n):

    arr = []
    distinct_arr = []
    for i in range(0,n):
        ele = int(input("Enter element in array"))
        arr.append(ele)

    for i in arr:
        if i not in distinct_arr:
            distinct_arr.append(i)
            
    return arr,distinct_arr

n = int(input("Enter length of array"))
print(distinct(n))
