#  Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#  If the string length is less than 2, return instead of the empty string
# 
# 
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String


def str3(str):

    temp =""


    if len(str)<2:
        return "Empty string"

    else:
        # return str[0:2]+str[-2:]

        for i in range(0,2):
            temp = temp+str[i]
        
        for i in range(len(str)-2,len(str)):
            temp = temp+str[i] #nn
        return temp


print(str3("w3resource"))
print(str3("w3"))
print(str3("Anuj More"))