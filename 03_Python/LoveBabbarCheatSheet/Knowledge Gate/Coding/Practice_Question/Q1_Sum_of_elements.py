#Wap to find sum of all elements in an array?


def sum_of_elements(n):

    arr = []
    sum = 0
    for i in range(0,n):
        ele = int(input())
        arr.append(ele)
        
    for j in range(0,len(arr)):
        sum +=arr[j]

    return sum
n = int(input("Please enter length of array"))
print("Sum of all the element in array is ",sum_of_elements(n))
