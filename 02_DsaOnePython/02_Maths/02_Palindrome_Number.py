class Solution:

    def palindrome(self,n):
        res  = 0
        temp = n
        while n:
            last = n % 10
            res = (res * 10) + last
            n = n // 10

        if temp == res: return True 
        else: return False


sol = Solution()
n = 1234321
print(sol.palindrome(n))