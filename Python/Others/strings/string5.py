# Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz''

lst = ['abc','xyz',"pqr"]
str = " "
for i in range(len(lst)-1,-1,-1):

    # str = str.append(lst[i])
    print(lst[i],end=" ")

