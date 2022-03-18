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
            # print(maxIndex1, arr[i], arr[maxIndex1])
            if maxIndex1 == -1 or arr[i] > arr[maxIndex1]:
                maxIndex1 = i

        # print(max1)

        for j in range(0, len):
            # print(maxIndex1, maxIndex2, arr[j], arr[maxIndex2])
            if j != maxIndex1 and (maxIndex2 == -1 or arr[j] > arr[maxIndex2]):
                maxIndex2 = j
        # print(max2)
        return arr[maxIndex1]*arr[maxIndex2]


len = int(input())
arr = list(map(int, input().split()))

print(maxProductFast(arr, len))

# Stress test


# def main():

# while (True):
#     n = random.randint(2, 9)
#     arr = []

#     for i in range(0, n):
#         arr.append(random.randint(0, 9))
#     # print(arr)

#     print(arr)
#     res1 = maxProduct(arr, len(arr))
#     res2 = maxProductFast(arr, len(arr))

#     if res1 == res2:
#         print("OK", res1, res2)
#     else:
#         print("Wrong", res1, res2)
#         break

# len = int(input())
# arr = list(map(int, input().split()))

# print(maxProductFast(arr, len(arr)))
# return True


# main()
