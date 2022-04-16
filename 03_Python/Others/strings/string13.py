# Write a Python program to count and display the vowels of a given text.


vowels = ["a","e","i","o","u"]

def vowels_counter(s):
    vowels_count = 0
    lst = []

    for i in range(0,len(s)):
        if s[i] in vowels:
            vowels_count+=1
            lst.append(s[i])
        

    return vowels_count,lst

print(vowels_counter("w3resource"))