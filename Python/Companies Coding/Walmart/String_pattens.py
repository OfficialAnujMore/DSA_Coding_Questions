def stringPattern(s1):

    combi = []
    # print(x)
    x = list(s1)
    count = 1
    for i in range(0, len(x)):
        for j in range(i, len(x)):

            if x[i] != x[j]:
                # print(i, x[i], j, x[j])
                x[i], x[j] = x[j], x[i]
                count +=1
                combi.append(x)
                x = list(s1)
    print(combi)
    return count
s1 = "sstt"
print(stringPattern(s1))
