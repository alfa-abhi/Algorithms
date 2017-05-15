"""
input: 5
output:
1 2 3 4 5
2 1 2 3 4
3 2 1 2 3
4 3 2 1 2
5 4 3 2 1
"""


matrix_size = input()
for i in xrange(0, matrix_size):
    for j in xrange(0, matrix_size):
        print str(abs(i - j) + 1),
    print

