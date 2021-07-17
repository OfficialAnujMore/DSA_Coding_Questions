# Write a Python program to check whether a string contains all letters of the alphabet.

a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
     "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"," "]



def check(s):

    for i in range(0,len(a)):
        if a[i]  in s:
            continue
        else:
            return False
    
    return True

s = "The quick brown fox jumps over the lazy dog"

print(check(s.lower()))