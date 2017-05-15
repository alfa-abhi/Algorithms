"""
input: 5
output:
[5, 5, 5, 5, 5]
[5, 4, 4, 4, 4]
[5, 4, 3, 3, 3]
[5, 4, 3, 2, 2]
[5, 4, 3, 2, 1]
"""


matrix_size = input()
matrix = [[0 for x in xrange(matrix_size)] for y in xrange(matrix_size)]
for i in xrange(0, matrix_size):
    for j in xrange(0, matrix_size):
        matrix[i][j] = matrix_size - j
        matrix[j][i] = matrix_size - j
for k in matrix:
    print k
