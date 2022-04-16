# wap to find the number of times a given word "the" appears in the given string

string = "The string where the word the present more than once"
word = 'the'

count = 0
st = string.split(' ')
#print(st)
for i in range(0,len(st)):
    if word == st[i]:
        count +=1
    
print(count)
