def linear_search(a,b):
    n = len(a)
    for i in range(n):
        if a[i] == b:
            return "Found the element ",b,"at position",i,"in array",a  
    return -1


a = list(map(int,input().split()))
b = int(input())
print(linear_search(a,b))

'''
Time complexity
O(n)
'''

