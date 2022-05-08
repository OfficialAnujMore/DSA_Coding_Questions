def reverse(str,n):
    if n == 0:
        return str[n]

    return str[n] + reverse(str, n-1)

def reverseStr(s):
    # l, r = 0, len(s)-1
    
    # while l <= r:
    #     s[l], s[r] = s[r], s[l]
    #     l+=1
    #     r-=1
    # print(s)

    def helper(s,l,r):
        if l >=r:
            return
        s[l], s[r] = s[r], s[l]

        helper(s,l+1, r-1)

    helper(s,l=0, r= len(s)-1)

    return s



# st = 'nitin'
# print(reverse(st,len(st)-1))
s = ["h","e","l","l","o"]
print(reverseStr(s))
