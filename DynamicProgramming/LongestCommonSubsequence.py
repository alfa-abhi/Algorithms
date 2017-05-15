major_sequence = list(raw_input())
minor_sequence = list(raw_input())
major_len = len(major_sequence)
minor_len = len(minor_sequence)
dp = [[0 for x in xrange(major_len)] for y in xrange(minor_len)]
direction = [[9 for m in xrange(major_len)] for n in xrange(minor_len)]
for j in xrange(major_len):
    if major_sequence[j] == minor_sequence[0]:
        for l in xrange(j, major_len):
            dp[0][l] += 1
        break
for i in xrange(1, minor_len):
    if minor_sequence[i] == major_sequence[0]:
        for l in xrange(i, minor_len):
            dp[l][0] += 1
        break
for i in xrange(1, minor_len):
    for j in xrange(1, major_len):
        if major_sequence[j] == minor_sequence[i]:
            dp[i][j] = dp[i-1][j-1] + 1
            direction[i][j] = 0
        else:
            if dp[i-1][j] >= dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                direction[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1]
                direction[i][j] = -1
seq = []
i = minor_len - 1
j = major_len - 1
while i > 0 or j > 0:
    if direction[i][j] == 0:
        seq.append(minor_sequence[i])
        i -= 1
        j -= 1
    elif direction[i][j] == -1:
        j -= 1
    elif direction[i][j] == 1:
        i -= 1
    else:
        if minor_sequence[i] == major_sequence[j]:
            seq.append(minor_sequence[i])
        break
print(seq[::-1])
