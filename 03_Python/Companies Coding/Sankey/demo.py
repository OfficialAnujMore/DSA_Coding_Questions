s1 = "silent"
s2 = 'listem'

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()
print(s1)
print(s2)

def is_anagram(s1, s2):
    ht = dict()
    
    if len(s1) != len(s2):
        return False
        
    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    
    
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
            
    for i in ht:
        if (ht[i] != 0):
            return False
        else:
            return True

if is_anagram(s1,s2):
    print("strings are anagrams")
else:
    print("strings are not anagrams")