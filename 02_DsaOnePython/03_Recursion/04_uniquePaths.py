'''
Notes:
- If n = 1 or m = 1 there is only one way to travel

Count all possible paths from top left to bottom right of a mXn matrix
'''

def uniquePaths(n,m):
# Base Case
    if n == 1 or m == 1:
        return 1
    else:
        return uniquePaths(n-1,m) + uniquePaths(n,m-1)

print(uniquePaths(3,3))
