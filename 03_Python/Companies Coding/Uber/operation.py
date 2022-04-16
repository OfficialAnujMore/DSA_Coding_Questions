# def optimalDeletions(arr1, p, q, r):

#     max_value = 0
#     sums = 1*p+2*q+3*r

#     # def bubble_sort(arr):
#     #     counter = 1
#     #     while (counter<len(arr)):
#     #         for i in range(0,len(arr)-counter):
#     #             if arr[i]>arr[i+1]:
#     #                 temp = arr[i]
#     #                 arr[i] = arr[i+1]
#     #                 arr[i+1] = temp
#     #         counter+=1
#     #     return arr

#     def merge_sort(a):
#         if len(a) > 1:
#             mid = len(a)//2
#             L = a[:mid]
#             R = a[mid:]
#             merge_sort(L)
#             merge_sort(R)
#             i = j = k = 0
#             while i < len(L) and j < len(R):
#                 if L[i] < R[j]:
#                     a[k] = L[i]
#                     i += 1
#                 else:
#                     a[k] = R[j]
#                     j += 1
#                 k += 1
#             while i < len(L):
#                 a[k] = L[i]
#                 i += 1
#                 k += 1
#             while j < len(R):
#                 a[k] = R[j]
#                 j += 1
#                 k += 1
#         return a
#     arr = merge_sort(arr1)

#     # print(arr)
#     # print(sums)
#     if sums > len(arr):
#         return 0
#     else:
#         # print(sums)
#         arr2 = arr[sums:]
#         print(arr2)
#         # i = 0
#         # while i < sums:
#         #     arr.pop(0)
#         #     i += 1
#         # # print(sums)
#         # return sum(arr)
#         return sum(arr2)

# arr = list(map(int,input().split()))
# p = int(input())
# q = int(input())
# r = int(input())


import time
t0 = time.time()
def optimalDeletions(arr1, p, q, r):

    max_value = 0
    sums = p+2*q+3*r
    arr1.sort()
    return sum(arr1[sums:])



arr = [-99, 62, -73, -78, -77, -65, -33, -68, 34, 63, 57, 10, 86, -31, -81, -79, 9, -91, -10, -84, -16, 56, -12, 12, 99, -53, 21, 40, -21, 22, -33, 16, 49, -71, -47, 75, 92, 5, -15, 41, 2, 64, -63, -78, 84, 10, -95, -2, 60, 24,
       92, -76, 94, 80, -38, 42, -8, -95, 9, 82, 59, 84, 57, -28, -70, -45, -91, -77, -47, -66, -83, -73, -19, 43, 35, 54, -1, 14, -70, -81, -83, -44, -95, -82, -10, -45, 58, 18, -6, 8, -96, -92, -4, -20, -97, 83, 83, 91, -22, 8]
p = 29
q = 4
r = 6

print(optimalDeletions(arr, p, q, r))
t1 = time.time()

total = t1-t0

print(total)

arr = [-99, 62, -73, -78, -77, -65, -33, -68, 34, 63, 57, 10, 86, -31, -81, -79, 9, -91, -10, -84, -16, 56, -12, 12, 99, -53, 21, 40, -21, 22, -33, 16, 49, -71, -47, 75, 92, 5, -15, 41, 2, 64, -63, -78, 84, 10, -95, -2, 60, 24,
       92, -76, 94, 80, -38, 42, -8, -95, 9, 82, 59, 84, 57, -28, -70, -45, -91, -77, -47, -66, -83, -73, -19, 43, 35, 54, -1, 14, -70, -81, -83, -44, -95, -82, -10, -45, 58, 18, -6, 8, -96, -92, -4, -20, -97, 83, 83, 91, -22, 8]
p = 29
q = 4
r = 6

print(optimalDeletions(arr, p, q, r))

'''



Given an array, you have to make some delete operations on it.

Delete any p elements from it.
Now delete q groups of 2 consecutive elements from the remaining array.
Now delete r groups of 3 consecutive elements from the remaining array.
After all these operations, the sum of elements of the resultant array should be the maximum possible.
Return this maximum value.

Example

For arr = [3, 1, 0, 5, 1, 6, 5, -1, -100], p = 1, q = 1, r = 1, the output should be
optimalDeletions(arr, p, q, r) = 16. Here, after deleting [1], [-1, -100] and [3, 1, 0], 
resultant array will be: [5, 6, 5], having sum = 5 + 6 + 5 = 16.

Here if we delete any other element, resultant sum will be less than 16. For eg, if we delete [3], [1, 0], [5, 1, 6], resultant array will be: [5, -1, -100], having sum = 5 + (-1) + (-100) = -96 which is less than 16.

[execution time limit] 4 seconds (py3)

[input] array.integer arr

Guaranteed constraints:
1 ≤ arr.length ≤ 100,
-105 ≤ arr[i] ≤ 105.

[input] integer p

[input] integer q

[input] integer r

Guaranteed constraints:
0 ≤ p, q, r ≤ 30,
p + 2q + 3r ≤ arr.length.

[output] integer

The maximum sum of elements of the resultant array after making required deletions.

Input:
arr: [3, 1, 0, 5, 1, 6, 5, -1, -100]
p: 1
q: 1
r: 1
Output:
undefined
Expected Output:
16
Console Output:
Empty
Error Output:
Empty









4





Input:
arr: [1, 4, 3, 5, 6, 8, 9, 9, 1]
p: 2
q: 2
r: 1
Output:
undefined
Expected Output:
0
Console Output:
Empty
Error Output:
Empty




Input:
arr: [1, 2, 3, -1]
p: 1
q: 1
r: 0
Output:
undefined
Expected Output:
3
Console Output:
Empty
Error Output:
Empty



Input:
arr: [11, 2, 8, 1, 3]
p: 0
q: 0
r: 1
Output:
undefined
Expected Output:
14
Console Output:
Empty
Error Output:
Empty




Input:
arr: [5, 10, 23]
p: 0
q: 0
r: 0
Output:
undefined
Expected Output:
38
Console Output:
Empty
Error Output:
Empty



Input:
arr: [1, 3, 2]
p: 2
q: 0
r: 0
Output:
undefined
Expected Output:
3
Console Output:
Empty
Error Output:
Empty



Input:
arr: [-99, 62, -73, -78, -77, -65, -33, -68, 34, 63, 57, 10, 86, -31, -81, -79, 9, -91, -10, -84, -16, 56, -12, 12, 99, -53, 21, 40, -21, 22, -33, 16, 49, -71, -47, 75, 92, 5, -15, 41, 2, 64, -63, -78, 84, 10, -95, -2, 60, 24, 92, -76, 94, 80, -38, 42, -8, -95, 9, 82, 59, 84, 57, -28, -70, -45, -91, -77, -47, -66, -83, -73, -19, 43, 35, 54, -1, 14, -70, -81, -83, -44, -95, -82, -10, -45, 58, 18, -6, 8, -96, -92, -4, -20, -97, 83, 83, 91, -22, 8]
p: 29
q: 4
r: 6
Output:
undefined
Expected Output:
2187
Console Output:
Empty
Error Output:
Empty




Input:
arr: [24838, -58545, 83279, 94970, 1385, 66383, 18777, -16892, -1974, -42194, -6768, -94636, 38220, -9764, 37012, -91083, 7967, 37236, 7074, -63818, 63157, 62002, -94222, -81924, -20985, -53835, -94650, -75675, -82300, -19892, 89609, 54539, 16803, 86073, 66108, -35039, 87554, 35939, -93165, -3784, 16561, -3589, -76540, 83961, 94742, -7369, -44329, 28631, 20743, -15242, 90959, 63579, 12861, -38287, -55353, 19231, -70415, -45079, -27823, 57989, 7223, -10540, 25774, 685, -10360, 92783, 48431, -3492, 64201, 29479, 38704, 46746, 14474, 36118, 12121, 48550, -77995, -78429, 54342, -32187, 65329, 62623, -38335, 65888, 41240, 36504, -48748, -27780, 48858, 2471, 71061, -31348, 900, -68762, -20210, 68722, -87425, -44355, -3469, 99823]
p: 30
q: 6
r: 8
Output:
undefined
Expected Output:
2211177
Console Output:
Empty
Error Output:
Empty



Given an array, return the minimum number of operations required to make all the elements of the array continuous. In one operation, any element of the array can be replaced with any integer.

Example

For arr = [6, 4, 1, 7, 10], the output should be
continuousElementsArray(arr) = 2.

In this example, the minimum number of operations needed to make all the elements of the array continuous is 2. You could replace 1 with 5 and 10 with 8 so that array will become arr = [6, 4, 5, 7, 8] which has continuous elelements.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer arr

Guaranteed constraints:
1 ≤ arr.length ≤ 105,
1 ≤ arr[i] ≤ 109,
All the elements in the array are distinct.

[output] integer

The minimum number of operations required to make all the elements of the array continuous.





Given an array, return the minimum number of operations required to make all the elements of the array continuous. In one operation, any element of the array can be replaced with any integer.

Example

For arr = [6, 4, 1, 7, 10], the output should be
continuousElementsArray(arr) = 2.

In this example, the minimum number of operations needed to make all the elements of the array continuous is 2. You could replace 1 with 5 and 10 with 8 so that array will become arr = [6, 4, 5, 7, 8] which has continuous elelements.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer arr

Guaranteed constraints:
1 ≤ arr.length ≤ 105,
1 ≤ arr[i] ≤ 109,
All the elements in the array are distinct.

[output] integer

The minimum number of operations required to make all the elements of the array continuous.



A vacuum cleaning robot is located at the charging station, which is at the top-left corner of the room.

The robot has a built-in map of the room, which is an m x n grid and a battery with limited capacity.

The floorPlan localizes obstacles and empty spaces, which are marked as 1 and 0 respectively in the grid. Initially, all the cells in the grid are dirty. Whenever the robot moves over a cell, it will clean the cell if it was dirty (It won't do anything if a cell is already cleaned).

Every time the robot executes a move (including leaving the charging station) the battery is reduced by 1. Note that the robot can move only in left, right, up and down. It cannot move diagonally.

The robot should return to the charging station before running out of battery. Write a function that returns the maximum number of cells that can be cleaned by the robot.

Example

Input:
floorPlan (grid)
0 0 0
0 1 0
0 0 0

Battery Capacity
6

Output:
3

Here robot can take the following path: (0, 0) -> (0, 1) -> (0, 2) -> (0, 1) -> (0, 0). Here 3 cells ((0, 0), (0, 1), (0, 2)) are cleaned and robot reaches back to (0, 0) before running out of battery.

Note that after (0, 2), if robot moves to (1, 2), it won't be able to reach the starting position before running out of battery, so it cannot clean that cell. Also, here (0, 0) -> (0, 1) -> (1, 1) -> (1, 0) -> (0, 0) is an invalid path because robot can't move on cell (1, 1) as it has obstacle.

[execution time limit] 4 seconds (py3)

[input] array.array.boolean floorPlan

[input] integer battery

Capacity of the battery

Guaranteed constraints:
1 ≤ floorPlan.length ≤ 10,
1 ≤ floorPlan[i] ≤ 10,
1 ≤ battery ≤ 12,
Charging station won't have obstacle

[output] integer

The maximum number of cells that can be cleaned. Note that the robot can't move on the cells having obstacles and should return to the charging station before running out of battery.

'''
