# Wapp to find the trasnpose of a matrix

def transpose(r,c):

    matrix = []
    transpose = []
    
    for i in range(r):
        row = []
        for j in range(c):
            element = int(input("Enter elements in matrix"))
            row.append(element)

        matrix.append(row)

#Printing matrix
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end = " ")
        print()
    print("*"*30)
# Creating transpose matrix

    for i in range(r):
        row = []
        for j in range(c):
            ele = 0
            row.append(ele)

        transpose.append(row)
            
# Transpose of matrix
    for i in range(r):
        for j in range(c):
            transpose[j][i] = matrix[i][j]


# Printing trasnpose matrix

    for i in range(r):
        for j in range(c):
            print(transpose[i][j],end=" ")
        print()


R = int(input("Enter number of rows"))
C = int(input("Enter number of columns"))

transpose(R,C)
