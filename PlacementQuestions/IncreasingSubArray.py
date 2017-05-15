# Input: 1 2 3 4 5 6 36 37 38 9 10 12 19
# Output: [36, 37, 38] 111


array = map(int, raw_input().split())
length = len(array)
maxStart = 0
maxEnd = 0
maxSum = 0
curSum = array[0]
curStart = 0
curEnd = 0
for x in xrange(1, length):
    if array[x] - array[x - 1] == 1:
        curSum += array[x]
        curEnd += 1
    else:
        if curSum > maxSum:
            maxSum = curSum
            maxStart = curStart
            maxEnd = curEnd
            curSum = array[x]
            try:
                curStart = x
                curEnd = curStart
            except IndexError:
                pass
print array[maxStart:maxEnd + 1], maxSum
