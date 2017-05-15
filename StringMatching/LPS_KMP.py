def most_common(lst):
    return max(set(lst), key=lst.count)

good_arr = []
np = map(int, raw_input().split())
arr = map(int, raw_input().split())
i = 0
j = 0
running_sum = 0
while i < np[0] and j < np[0]:
    running_sum = sum(arr[i:j+1])
    if running_sum < np[1]:
        try:
            good_arr.append(most_common(arr[i:j+1]))
        except ValueError:
            pass
        j += 1
    else:
        i += 1
        j -= 1
good_arr.append(arr[np[0]-1])
print most_common(good_arr)
