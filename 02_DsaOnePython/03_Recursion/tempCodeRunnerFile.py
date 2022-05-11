def josephusProblem(n,k):
    if n == 1:
        return 0

    return (josephusProblem(n-1,k) + k) % n


arr = 7
k = 3
print('return',josephusProblem(arr,k))