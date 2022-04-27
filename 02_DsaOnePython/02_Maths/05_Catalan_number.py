# Time complexity of above implementation is equivalent to nth catalan number. 

class Solution:
    def catalanNo(self,n):
        if n <= 1:
            return 1
        res = 0
        for i in range(n):
            res += self.catalanNo(i) * self.catalanNo(n-i-1)
        return res


sol = Solution()
print(sol.catalanNo(9))