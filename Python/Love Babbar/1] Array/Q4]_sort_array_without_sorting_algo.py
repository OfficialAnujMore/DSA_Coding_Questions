# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo


def sort(arr):
    new_arr = []

    while arr:
        min_ele = arr[0]
        for ele in arr:
            if ele < min_ele:
                min_ele = ele
        new_arr.append(min_ele)
        arr.remove(min_ele)
    print(new_arr)
    largest(new_arr)

def largest(arr):
    for i in range(len(arr)-1,-1,-1):
        print(arr[i],end = "")




#arr = [0,1,0]
arr = [4,5,15,67,23]
sort(arr)


