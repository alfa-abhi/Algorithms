"""
input:
4
0 1 2 3 4
5 6 7 8 9
10 11 12 13 14
15 16 17 18 19
output:
[0, 5, 10, 15, 16, 11, 6, 1, 2, 7, 12, 17, 18, 13, 8, 3, 4, 9, 14, 19]
"""


n = input("Number of rows: ")
matrix = []
for x in xrange(0, n):
    row = map(int, raw_input().split())
    matrix.append(row)
wave = []
for y in xrange(0, len(matrix[0])):
    if y % 2 == 0:
        for x in xrange(0, n):
            wave.append(matrix[x][y])
    else:
        for x in xrange(n-1, -1, -1):
            wave.append(matrix[x][y])
print wave