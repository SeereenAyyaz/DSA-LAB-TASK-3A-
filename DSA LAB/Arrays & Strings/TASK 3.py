def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Original Matrix:")
for row in matrix:
    print(row)
rotate_matrix(matrix)
print("\nRotated Matrix (90° Clockwise):")
for row in matrix:
    print(row)
