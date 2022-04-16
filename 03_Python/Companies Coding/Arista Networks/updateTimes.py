def updateTimes(a1, a2):

    n = len(a1)
    m = len(a2)
    i = 0
    j = 0
    maxequal = 0
    previous = []

    while i < n and j < m:

        previous.sort()
        x = len(previous)
        print(a1[i],a2[j])
        if x != 0:
            print(previous[x-1])
            if a1[i] == a2[j] and a1[i] not in previous and a1[i] > previous[x-1]:
                previous.append(a1[i])
                maxequal += 1
                i += 1
                j += 1
            else:
                i += 1
                j += 1
        elif (a1[i] == a2[j] and a1[1] not in previous):
            previous.append(a1[i])
            maxequal += 1
            i += 1
            j += 1
        else:
            i+=1
            j+=1

    return maxequal


a1 = [100, 20, 74, 28, 17, 39, 56, 56, 91, 75, 69, 16, 84, 31, 21, 100, 56, 94, 34, 59, 95, 28, 30, 92, 41, 70, 61, 28, 66, 50, 58, 38, 94, 37, 18, 23, 99, 17, 5, 28, 18, 63, 51, 13, 9, 79, 8, 4, 12, 3,
      32, 3, 88, 67, 27, 14, 95, 92, 76, 79, 70, 12, 100, 70, 39, 47, 15, 9, 93, 68, 92, 26, 65, 1, 92, 63, 82, 11, 100, 38, 98, 100, 14, 6, 95, 4, 83, 86, 74, 23, 87, 76, 4, 77, 14, 58, 40, 16, 97, 37, 8]
a2 = [47, 20, 74, 15, 17, 77, 56, 56, 91, 67, 28, 16, 54, 30, 67, 14, 56, 94, 35, 59, 71, 19, 32,
      92, 41, 84, 59, 28, 66, 50, 77, 38, 26, 37, 18, 23, 99, 44, 5, 21, 23, 63, 43, 13, 9, 79, 8, 91]
print(updateTimes(a1, a2))
