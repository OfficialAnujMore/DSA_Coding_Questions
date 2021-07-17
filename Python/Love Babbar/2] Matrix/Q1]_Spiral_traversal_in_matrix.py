# Spiral traversal on a Matrix



r = int(input("Enter number of rows : "))
c = int(input("Enter number of columns :"))

matrix = []


for i in range(r):
    row = []
    for j in range(c):
        ele = int(input("Enter elements :"))
        row.append(ele)
    matrix.append(row)

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end = " ")
    print()

#sprial traversal

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end="")
        