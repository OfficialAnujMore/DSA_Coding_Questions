# Wapp to find the kth smallest element in an array



def kth_element(arr,k):

    while arr:
        min_element = arr[0]
        for ele in arr:
            if ele < min_element:
                min_element = ele

        new_arr.append(min_element)
        arr.remove(min_element)

    
    return new_arr[k-1]





arr = [7, 10, 4, 3, 20, 15]
k = 3
new_arr = []
print(kth_element(arr,k))


