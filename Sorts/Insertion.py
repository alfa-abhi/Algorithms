import timeit

arr = map(int, raw_input().split())
start = timeit.default_timer()
n = len(arr)
temp = [0]
for i in xrange(1, n):
    temp[0] = arr[i]
    j = 0
    while j < i:
        if temp[0] < arr[j]:
            # print(arr[0:j], temp, arr[j:i], arr[i+1:])
            arr = arr[0:j] + temp + arr[j:i] + arr[i+1:]
            break
        j += 1
    # print arr
end = timeit.default_timer()
print(end - start)
print(arr)
