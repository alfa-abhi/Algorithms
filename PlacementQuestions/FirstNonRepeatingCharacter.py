string = list(raw_input())
length = len(string)
megaFlag = False
for k in xrange(0, length):
    flag = False
    for j in xrange(0, length):
        if string[k] == string[j] and k != j:
            flag = True
            break
    if not flag:
        print string[k]
        megaFlag = True
        break
if not megaFlag:
    print "Every character has a repetition."
