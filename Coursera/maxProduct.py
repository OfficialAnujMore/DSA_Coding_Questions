import random


def maxProduct(arr, len):
    result = 0

    for i in range(0, len):
        for j in range(i+1, len):
            product = arr[i]*arr[j]

            if product > result:
                result = product

    return result


def maxProductFast(arr, len):

    maxIndex1 = -1
    maxIndex2 = -1

    if len == 2:
        return arr[0]*arr[1]
    else:

        for i in range(0, len):
            if arr[i] > arr[maxIndex1]:
                maxIndex1 = i

        # print(max1)

        for j in range(0, len):
            if j != maxIndex1 and arr[j] > arr[maxIndex2]:
                maxIndex2 = j
        # print(max2)
        return arr[maxIndex1]*arr[maxIndex2]


# Stress test
def main():

    while (True):
        n = random.randint(2, 9)
        arr = []

        for i in range(0, n):
            arr.append(random.randint(0, 9))
        # print(arr)

        # len = int(input())
        # arr = list(map(int, input().split()))
        print(arr)
        res1 = maxProduct(arr, len(arr))
        res2 = maxProductFast(arr, len(arr))

        if res1 == res2:
            print("OK", res1, res2)
        else:
            print("Wrong", res1, res2)
            break

    return True


main()
