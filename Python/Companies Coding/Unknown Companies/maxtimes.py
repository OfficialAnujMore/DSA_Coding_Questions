def maxTime(a):
    dict = {}

    for i in a:
        keys = dict.keys()
        if i in keys:
            dict[i]+=1
        else:
            dict[i] = 1

    max = 1
    str = ''
    for i in dict:
        if dict[i] > max:
            str+=i

    return str
a = 'test'
print(maxTime(a.lower()))