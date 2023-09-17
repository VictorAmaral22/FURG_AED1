# 1) Leia uma matriz e mostre na tela no formato para humanos (bonitinho)
def matrixValidator (matrix):
    colCounter = len(matrix[0])
    valid = True
    for line in matrix[1:]:
        if colCounter != 0 and len(line) != colCounter:
            valid = False
            break

    return valid

def printMatrix (matrix):
    isValid = matrixValidator(matrix)

    if isValid:
        for line in matrix:
            print("| ",end="")
            for col in line:
                print(str(col),end=" ")
            print("|")
    else:
        print("Matriz inválida")

# matrix = [
#     [1,2,3],
#     [1,2,4],
#     [1,2,3],
# ]

# printMatrix(matrix)


# 2) Leia uma matriz e descubra os determinantes

matrix1 = [
    [1, 0, -3],
    [14, 9, 0],
    [2, 5, -7]
]

printMatrix(matrix1)

c = 0
dPos = 0
dNeg = 0

while c < len(matrix1[0]):
    if c+1 > len(matrix1[0]):
        dPos += matrix1[0][c] + matrix1[1][0] + matrix1[2][1]
        c += 1
    else:
        if c+2 > len(matrix1[0]):
            dPos += matrix1[0][c] + matrix1[1][0] + matrix1[2][1]
            c += 1
        else:
            dPos += matrix1[0][c] + matrix1[1][c+1] + matrix1[2][c+2]
            c += 1

print(dPos)
    
