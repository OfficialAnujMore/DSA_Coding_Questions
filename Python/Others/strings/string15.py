# Write a Python program to find the maximum occurring character in a given string.


def check(str):

    dict = {}

    for i in s:
        keys = dict.keys()
        if i in keys:
            dict[i]+=1
        else:
            dict[i]=1


    max_key = max(dict,key=dict.get)
    max_value = max(dict.values())

    return max_key,max_value

  

s  = "Annujjj"
print(check(s))