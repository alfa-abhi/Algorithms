"""
Input: -1 2 -3 4 5 -1 4 -3
Output: 12
"""


input_array = map(int, raw_input().split())
megaMax = -999999
curMax = 0
for x in input_array:
    curMax += x
    if curMax > megaMax:
        megaMax = curMax
    if curMax < 0:
        curMax = 0
print megaMax