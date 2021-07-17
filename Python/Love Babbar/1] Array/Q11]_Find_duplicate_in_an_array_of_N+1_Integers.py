# find duplicate in an array of N+1 Integers


a = [1,2,3,4,2]

seen = set()

for i in a:
    if i in seen:
        print(i)

    seen.add(i)
