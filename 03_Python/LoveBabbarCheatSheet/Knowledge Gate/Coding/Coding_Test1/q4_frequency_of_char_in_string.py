string  = "This is a test string"

char = 'i'

count = 0

for i in range(0,len(string)):
    if char == string[i]:
        count+=1

print(count)
