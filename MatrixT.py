mat1 = [[1, 2], [3, 4], [5, 6]]


mat1_rows = len(mat1)
mat1_cols = len(mat1[0])
mat1T = [[[0] for i in range(mat1_rows)] for j in range(mat1_cols)]

for i in range(mat1_rows):
        for j in range(mat1_cols):
                mat1T[j][i] = mat1[i][j]

print(mat1T)

