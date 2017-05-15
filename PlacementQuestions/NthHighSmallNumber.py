def k_small(arr, left, right, kth):
    if 0 < kth <= right - left + 1:
        position = partition(arr, left, right)
        if position == kth - 1:
            return arr[position]
        if position > kth - 1:
            return k_small(arr, left, position - 1, kth)
        else:
            return k_small(arr, position + 1, right, kth - position + left - 1)
    return -1


def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in xrange(l, r):
        if arr[j] <= x:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[r], arr[i] = arr[i], arr[r]
    return i

array = map(int, raw_input().split())
length = len(array)
k_index = input()
print "Kth Smallest: " + str(k_small(array, 0, length - 1, k_index))
print "Kth Highest: " + str(k_small(array, 0, length - 1, length - k_index + 1))
