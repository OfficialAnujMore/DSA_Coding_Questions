r = int(input("Enter number of rows in matrix : "))
c = int(input("Enter number of columns in matrix : "))

matrix = []
eve = []
odd = []

# Input elements for matrix
for i in range(r):
    row = []
    for j in range(c):
        ele = int(input("Enter element: "))
        row.append(ele)
    matrix.append(row)
print(matrix)

# printing elements of matrix
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()


for i in range(r):
    for j in range(c):

        if matrix[i][j]%2==0:
            eve.append(matrix[i][j])
        else:
            odd.append(matrix[i][j])

print("Even element in matrix are :",eve)
print("Odd elements in matrix are :",odd)