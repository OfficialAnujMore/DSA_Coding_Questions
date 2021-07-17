r = int(input("Enter number of rows in matrix : "))
c = int(input("Enter number of columns in matrix : "))

matrix = []

# taking input for matrix
for i in range(r):
    row = []
    for j in range(c):
        ele = int(input("Enter element in matrix : "))
        row.append(ele)
    matrix.append(row)

# printing elements in matrix

print("ELements of matrix are: ")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end = " ")
    print()

# Sum of rows and column 

for i in range(r):
    sum = 0
    for j in range(c):
        sum += matrix[i][j]
    print("Sum of element is " ,sum)
        


