# Move all the negative elements to one side of the array


def rearrange(arr):
    new_arr = []

    while arr:
        min_ele = arr[0]
        for ele in arr:
            if ele < min_ele:
                min_ele = ele
        new_arr.append(min_ele)
        arr.remove(min_ele)
    print(new_arr)




#arr = [0,1,0]
 = [0, -2, 1, -892, 0]

rearrange(arr)
