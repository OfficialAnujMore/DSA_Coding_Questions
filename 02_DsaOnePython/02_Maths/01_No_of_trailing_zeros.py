# To find number of trailing zeros in n!
class Solution:

    def count(self, n):
        res = 0
        i = 5

        while i <= n:
            res = res + (n//i)
            i *= 5

        return res


sol = Solution()
n = int(input('Enter a number '))
print('The number of trailing zeros in ', n,'!', 'are', sol.count(n))
