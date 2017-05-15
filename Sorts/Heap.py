import timeit


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in xrange(n, -1, -1):
        heapify(arr, n, i)
    for x in xrange(n-1, 0, -1):
        arr[x], arr[0] = arr[0], arr[x]
        heapify(arr, x, 0)


arr = map(int, raw_input().split())
start = timeit.default_timer()
heap_sort(arr)
end = timeit.default_timer()
print(end - start)
print(arr)
