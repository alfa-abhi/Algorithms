import timeit


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in xrange(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[high], arr[i+1] = arr[i+1], arr[high]
    return i+1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


arr = map(int, raw_input().split())
start = timeit.default_timer()
quick_sort(arr, 0, len(arr)-1)
end = timeit.default_timer()
print(end - start)
print(arr)
