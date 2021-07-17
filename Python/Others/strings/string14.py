# Write a Python program to move * to the front of a given string.

def mover(s):

    str1 = ""
    str2 = ""
    for i in range(0,len(s)):
        if s[i] == "*":
            str1+="*"
        else:
            str2+=s[i]
    return str1 + str2

s = "an*j*"
print(mover(s))
print(mover("w3resource*.**com**"))