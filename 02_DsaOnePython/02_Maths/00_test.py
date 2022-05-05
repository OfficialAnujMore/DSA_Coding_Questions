nums = [1,2,3,4,5,6,7]
k = 3

n, k, j = len(nums), k % len(nums), 0
while n > 0 and k % n != 0:
    for i in range(0, k):
        print(nums[j + i], nums[len(nums) - k + i])
        nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i] # swap
    n, j = n - k, j + k
    k = k % n

print(nums)