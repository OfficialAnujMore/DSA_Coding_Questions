# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# #
# # Complete the 'groupSort' function below.
# #
# # The function is expected to return a 2D_INTEGER_ARRAY.
# # The function accepts INTEGER_ARRAY arr as parameter.
# #
# import operator

# def groupSort(arr):
#     d ={}
#     res = []
#     demo = [[0,2]]

#     for i in arr:

#         keys = d.keys()

#         if i in keys:
#             d[i]+=1
#         else:
#             d[i]=1

#     print("Main Dict",d)

#     sorted_d = dict(sorted(d.items(),key=operator.itemgetter(1), reverse = True))


# #     Main Dict {13: 9, 1: 7, 6: 7, 5: 10, 15: 4, 14: 4, 18: 5, 2: 6, 9: 2, 11: 5, 4: 4, 12: 6, 17: 6, 7: 4, 20: 6, 8: 7, 3: 2, 19: 3, 16: 2, 10: 1}
# # Sorted {5: 10, 13: 9, 1: 7, 6: 7, 8: 7, 2: 6, 12: 6, 17: 6, 20: 6, 18: 5, 11: 5, 15: 4, 14: 4, 4: 4, 7: 4, 19: 3, 9: 2, 3: 2, 16: 2, 10: 1}


#     for i in sorted_d:
#         if sorted_d.get(i)>sorted_d.get(i+1):
#             res.append([i,sorted_d.get(i)])
#         else:
#             if sorted_d.get(i) == sorted_d.get(i+1):
#                 backup_i = i
#                 res.pop(len(res)-1)


#         print("")


# #         100
# # 13
# # 1
# # 6
# # 5
# # 15
# # 14
# # 18
# # 2
# # 9
# # 1
# # 5
# # 11
# # 1
# # 4
# # 13
# # 11
# # 5
# # 12
# # 17
# # 1
# # 17
# # 14
# # 7
# # 4
# # 20
# # 7
# # 2
# # 2
# # 17
# # 13
# # 17
# # 15
# # 11
# # 20
# # 8
# # 12
# # 17
# # 13
# # 18
# # 12
# # 15
# # 1
# # 5
# # 6
# # 2
# # 5
# # 3
# # 6
# # 13
# # 8
# # 8
# # 5
# # 6
# # 19
# # 13
# # 13
# # 4
# # 15
# # 4
# # 8
# # 20
# # 13
# # 12
# # 14
# # 17
# # 16
# # 5
# # 1
# # 7
# # 6
# # 5
# # 19
# # 18
# # 7
# # 14
# # 8
# # 19
# # 10
# # 6
# # 5
# # 12
# # 6
# # 12
# # 18
# # 8
# # 5
# # 20
# # 11
# # 2
# # 1
# # 3
# # 13
# # 16
# # 9
# # 2
# # 8
# # 20
# # 11
# # 20
# # 18


#           # print(sorted_d)
#     # for i in sorted_d:
#     #     print(i,sorted_d.get(i))
#     #     a = []
#     #     a.append(i)
#     #     a.append(sorted_d.get(i))
#     #     res.append(a)


#     return res

#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = []

#     for _ in range(arr_count):
#         arr_item = int(input().strip())
#         arr.append(arr_item)

#     result = groupSort(arr)

#     fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
#     fptr.write('\n')

#     fptr.close()
