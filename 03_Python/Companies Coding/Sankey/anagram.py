def anagram(s1, s2):
    n = len(s1)
    m = len(s2)
    i = 0
    j = 0
    count = 0
    flag = "Anagram"
    if n == m:
        while i < n and j < m:
            print(s1[i], s2[j])
            if s1[i] == s2[j]:
                i += 1
                j = 0
                count += 1
            elif (j == m-1):
                i = n
                flag = "Not anagram"
            else:
                j += 1
    else:
        flag = "Not anagram"

    return flag


# s1 = "cat"
# s2 = 'bat'
s1 = "silent"
s2 = 'listen'
print(anagram(s1, s2))
