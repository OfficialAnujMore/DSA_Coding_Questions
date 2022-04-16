# Find Duplicate characters in a string


str = 'i am checking this string to see how many times each character appears'.replace(" ",'')
#str = "ANUjAAAA"
count = {}
for i in str:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

print(count)

for i in count:
    if count[i]>1:
        print("Count of",i,"is",count[i])
