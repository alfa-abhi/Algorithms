# Find if a number a[i] == i in a given sorted array exist, if yes, print the number.
# input: 11 15 4 -1 -2 -3 0 9 12 (sorted by machine before any computation.)
# complexity: (O(log(n))
# output: 4


def enhanced_binary_search(arr, start, end):
    mid = (end - start + 1) / 2
    if arr[mid] == mid:
        return arr[mid]
    if arr[mid] > mid:
        return enhanced_binary_search(arr, start, mid)
    else:
        return enhanced_binary_search(arr, mid+1, end)


array = map(int, raw_input().split())
array.sort()
print array
print enhanced_binary_search(array, 0, len(array) - 1)
