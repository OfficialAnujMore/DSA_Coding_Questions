def permutations(arr):

    finalArr = []
    resArr = arr
    i = 0
    while i < len(arr)-1:
        if i == len(arr) -2:
            finalArr.append(resArr)
            resArr = arr
        else:
            temp = resArr[i]
            resArr[i] = resArr[i+1]
            resArr[i+1] = temp
            i+=1


    return finalArr

arr = [ i for i in range(0,10)]
print(permutations(arr))