# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}


# def str2(str):

#     dict = {}

#     for i in str:
#         keys = dict.keys()
#         if i in keys:
#             dict[i]+=1

#         else:
#             dict[i]=1

#     return dic


def str2(str):
    dict = {}

    for i in str:
        keys = dict.keys()
        if i in keys:
            dict[i]+=1
        else:
            dict[i] = 1
    return dict


print(str2("google.com"))