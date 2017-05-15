"""
input: 5
output:
[1, 2, 3, 4, 5]
[2, 3, 4, 5, 6]
[3, 4, 5, 6, 7]
[4, 5, 6, 7, 8]
[5, 6, 7, 8, 9]
"""


matrix_size = input()
matrix = [[0 for x in xrange(matrix_size)] for y in xrange(matrix_size)]
for i in xrange(matrix_size):
    for j in xrange(matrix_size):
        matrix[matrix_size - i - 1][j] = matrix_size - i + j
        matrix[i][matrix_size - j - 1] = matrix_size - j + i
for k in matrix:
    print k
