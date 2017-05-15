import timeit


def merge(arr, left, middle, right):
    n1_size = middle - left + 1
    n2_size = right - middle
    left_array = [0] * n1_size
    right_array = [0] * n2_size
    for i in xrange(0, n1_size):
        left_array[i] = arr[left+i]
    for i in xrange(0, n2_size):
        right_array[i] = arr[middle+i+1]
    i = 0
    j = 0
    k = left
    while i < n1_size and j < n2_size:
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1
    while i < n1_size:
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < n2_size:
        arr[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r - 1) / 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid+1, r)
        merge(arr, l, mid, r)


arr = map(int, raw_input().split())
start = timeit.default_timer()
merge_sort(arr, 0, len(arr)-1)
end = timeit.default_timer()
print(end - start)
print(arr)
