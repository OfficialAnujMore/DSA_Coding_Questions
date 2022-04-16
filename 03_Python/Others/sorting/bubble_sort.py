def bubble_sort(arr):
    counter = 1
    while(counter<len(arr)):
        for i in range(0,len(arr)-counter):
            if (arr[i]>arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

        counter+=1
    return arr

arr = list(map(int, input().split()))
arr = [12,45,1,3,99,223,21123,5553,1,2343]
bubble = bubble_sort(arr)
print(bubble)
'''
Time complexity 
Best = O(n)
Average, Worst = O(n**2)
Worst and Average Case Time Complexity: Worst case occurs 
when array is reverse sorted.
'''