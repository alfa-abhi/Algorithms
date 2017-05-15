import timeit

arr = map(int, raw_input().split())
start = timeit.default_timer()
n = len(arr)
temp = [0]
for i in xrange(0, n):
    temp[0] = min(arr[i:])
    index = arr.index(temp[0])
    arr = arr[0:i] + temp + arr[i:index] + arr[index+1:]
    # print arr
end = timeit.default_timer()
print(end - start)
print(arr)
