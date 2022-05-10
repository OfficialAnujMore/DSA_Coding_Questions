def josephusProblem(n,i,k):
    if len(n) == 1:
        return n[0]
    if i == len(n):
        i = 0
    match = 0
    while i < k:
        if i == len(n)-1:
            i = 0
        else:
            match+=1
            i+=1
        if match == k-1:
            print(i)
            n.pop(i)
            break
    return josephusProblem(n,i,k)



arr = [0,1,2,3]
k = 3
i = 0
print('return',josephusProblem(arr,i,k))