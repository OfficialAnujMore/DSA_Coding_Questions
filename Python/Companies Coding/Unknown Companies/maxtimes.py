def maxTime(a):
    dict = {}

    for i in a:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    max = 1
    str = ''
    for i in dict:
        if dict[i] > max:
            str += i

    return str
a = 'test'
print(maxTime(a.lower()))


'''
        for i in range(0,len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i],0)
            dictT[t[i]] = 1 + dictT.get(t[i],0)
'''
