def twoSum(nums, target):
    res = []
    start = 0
    end = len(nums)

    mid = len(nums)//2
    while start < end:
        diff = target - nums[start]
        if diff in nums[start+1:end]:
            print(mid, nums[mid])

            if nums[mid] == diff:
                res.append(nums[start])
                res.append(nums[mid])
            if nums[mid] > diff:
                mid = len(nums[mid:])//2
                end = mid
            else:
                mid = len(nums[:mid])//2
                end = mid
        else:
            start += 1

    return res


arr = [2, 7, 11, 15]
n = 9
print(twoSum(arr, n))
