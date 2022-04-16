def wave(arr, n):

    i = 0

    if n % 2 == 0:

        while i < n:
            A[i], A[i+1] = A[i+1], A[i]
            i += 2
    else:
        while i < n-1:
            A[i], A[i+1] = A[i+1], A[i]
            i += 2
    return A


A = [2, 4, 7, 8, 9, 10]
print(wave(A, len(A)))
