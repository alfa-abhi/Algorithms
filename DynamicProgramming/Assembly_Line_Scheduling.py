test_cases = input()
for _ in xrange(test_cases):
    len_of_line = input()
    line1 = map(int, raw_input().split())
    line2 = map(int, raw_input().split())
    if len_of_line != 1:
        line1to2 = map(int, raw_input().split())
        line2to1 = map(int, raw_input().split())
    else:
        line1to2 = [0]
        line2to1 = [0]
    t1 = [0 for y in xrange(len_of_line)]
    t2 = [0 for z in xrange(len_of_line)]
    t1[0] = line1[0]
    t2[0] = line2[0]
    for i in xrange(1, len_of_line):
        t1[i] = min(t1[i-1] + line1[i], t2[i-1] + line2to1[i-1] + line1[i])
        t2[i] = min(t2[i-1] + line2[i], t1[i-1] + line1to2[i-1] + line2[i])
    print(min(t1[len_of_line-1], t2[len_of_line-1]))

# Test Case
# 2
# 2
# 15 6
# 5 21
# 1
# 7
# 3
# 7 2 5
# 5 2 4
# 7 6
# 2 2
