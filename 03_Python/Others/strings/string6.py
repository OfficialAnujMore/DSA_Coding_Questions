#  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged.

# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'


def adder(str):

    if len(str)<3:
        return str
    elif "ing" in str:
        return str + "ly"
    else:
        return str+"ing"


a = input()
print(adder(a))