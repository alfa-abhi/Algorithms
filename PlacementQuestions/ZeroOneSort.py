# input: 0 1 0 1 1 1 0 0 1 0
# output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]


array = map(int, raw_input().split())
zeros = array.count(0)
for x in xrange(0, len(array)):
    if x < zeros:
        array[x] = 0
    else:
        array[x] = 1
print array
