# binary search
from ctypes.wintypes import tagRECT


def twoSum(numbers, target):
    for i in range(len(numbers)):
        l, r = i+1, len(numbers)-1
        tmp = target - numbers[i]
        while l <= r:
            print(l,r, (r-l))
            mid = l + (r-l)//2
            print(mid)
            if numbers[mid] == tmp:
                return [i+1, mid+1]
            elif numbers[mid] < tmp:
                l = mid+1
            else:
                r = mid-1


arr = [3,24,50,79,88,150,345]
target = 200
print(twoSum(arr, target))
