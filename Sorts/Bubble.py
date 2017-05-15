import timeit
arr = map(int, raw_input().split())
start = timeit.default_timer()
n = len(arr)
for i in xrange(0, n):
    for j in xrange(0, n - i - 1):
        if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # print arr
end = timeit.default_timer()
print(end - start)
print(arr)
