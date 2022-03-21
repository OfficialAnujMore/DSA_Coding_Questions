def fun(strs):
    n = len(strs)
    initial = 1
    finalPrefix = ''
    i = 1

    if n <= 1:
        finalPrefix = strs[0]
        return finalPrefix

    while i <= n:

        if (i % n == 0):
            initial += 1
            i = 0
        prefix = strs[0][0:initial]

        print(strs[i])
        nthPrefix = strs[i][0:initial]
        print(prefix, nthPrefix)
        if nthPrefix != prefix:
            finalPrefix = prefix[0:len(prefix)-1]

            break
        if len(prefix) == len(strs[0]):
            finalPrefix = prefix[0:len(prefix)]
            break
        else:
            i += 1

    return finalPrefix


strs = ["flower", "flower", "flower", "flower"]
print("answer", fun(strs))
