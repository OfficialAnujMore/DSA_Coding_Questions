
a = [[1, 2, 3],
    [3, 4, 5],
    [7, 6, 4]]

b = [[5, 2, 6],
    [5, 6, 7],
    [7, 6, 4]]

c = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        
        for k in range(len(b)):
            
            c[i][j] += a[i][k]*b[k][j]

print(c)
