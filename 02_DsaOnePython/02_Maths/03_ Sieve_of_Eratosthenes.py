# Prime no in a given range
# TC: n*log(log(n))
# SC: O(n)
class Solution:

    def primes(self, arr):
        # Finding square root
        sqrt = int(len(arr)**0.5)
        print(sqrt)
        res = []

        booleanArray = []
        booleanArray = [True for i in range(len(arr))]
        booleanArray[0] = False
        for i in range(1, sqrt):
            for j in range(i+1, len(arr)):
                if (arr[j] % arr[i]) == 0:
                    booleanArray[j] = False

        print(booleanArray)
        for k in range(0, len(booleanArray)):
            if booleanArray[k] == True:
                res.append(arr[k])

        return res


sol = Solution()
endingValue = int(input('Enter the ending value: '))
arr = [i for i in range(1, endingValue)]
# [True, False, False, True, False, True, False, True, True, True, False, True]
print('Prime numbers in range 1,', 'range', 'are', sol.primes(arr))
