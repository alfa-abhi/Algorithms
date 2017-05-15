# input: 9,4,-3,-2,1,-1,5,7,-9,-5
# output: 9, 4, 1, 5, 7, -3, -2, -1, -9, -5

array = map(int, raw_input().split(","))
pos_counter = 0
for k in array:
    if k >= 0:
        pos_counter += 1

separate_list = [0 for x in xrange(len(array))]
pos = 0
neg = pos_counter
counter = 0
while counter < len(array):
    if array[counter] >= 0:
        separate_list[pos] = array[counter]
        pos += 1
    else:
        separate_list[neg] = array[counter]
        neg += 1
    counter += 1
print separate_list

