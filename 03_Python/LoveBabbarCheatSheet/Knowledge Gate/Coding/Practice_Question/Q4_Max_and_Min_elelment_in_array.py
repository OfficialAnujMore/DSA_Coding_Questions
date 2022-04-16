# Wapp to find max and min element in python


def max_and_min(n):

    a = []
    for i in range(0,n):
        ele = int(input("Enter element in array:"))
        a.append(ele)

    print("The array is: ",a)

    max = a[0]
    min = a[0]

    for i in range(0,len(a)):
        if a[i]>max:
            max = a[i]

        if a[i]<min:
            min = a[i]

    print("The maximum element in the given array is ",max,"and the minimum element is ",min)
   
n = int(input("Enter length of array: "))

print(max_and_min(n))
