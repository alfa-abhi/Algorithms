# input: 11010011
# output: [1, 1, 0, 1, 0, 0]


seq = map(int, list(raw_input()))
length = len(seq)
zero = seq.count(0)
one = length - zero
equator = min(zero, one)
counter = 0
oneCount = 0
zeroCount = 0
subSequence = []
while counter < length:
    if seq[counter] == 1:
        if oneCount < equator:
            subSequence.append(1)
            oneCount += 1
    else:
        if zeroCount < equator:
            subSequence.append(0)
            zeroCount += 1
    counter += 1
print subSequence


