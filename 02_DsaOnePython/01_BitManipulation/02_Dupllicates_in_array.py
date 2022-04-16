''' 
1. 0 ^ n = n
2. n ^ n =  0

TC: O(n)
SC: O(1)
'''
def findDuplicate(arr):
    res = 0

    for i in arr:
        res = res ^ i

    return res


def findTwoDuplicates(arr):
    a,b =0,0
    res = 0

    for i in arr:
        res = res ^ i
    temp = res
    res = (res & -res)
    print(res)


arr = [5,4,1,4,3,5,1,2]

# print(findDuplicate(arr))
print(findTwoDuplicates(arr))