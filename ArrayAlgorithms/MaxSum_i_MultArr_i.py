def max_sum(arr):
    arrSum = 0
    currVal = 0
    n = len(arr)
    for i in range(0, n):
        arrSum += arr[i]
        currVal += i * arr[i]
    maxVal = currVal
    for j in range(1, n):
        currVal = currVal + arrSum - n * arr[n - j]
        if currVal > maxVal:
            maxVal = currVal
    return maxVal


arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print "Max sum is: ", max_sum(arr)
