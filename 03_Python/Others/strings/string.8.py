#  Write a Python program to remove the nth index character from a nonempty string.



def remove(s,ind):
    for i in range(0,len(s)):
        if (i == ind):
            s = s.replace(s[i],"")
            return s

print(remove("Anuja",4))
print(remove("Python",0))
print(remove("Python",3))
print(remove("Python",5))