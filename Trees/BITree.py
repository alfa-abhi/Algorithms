def updateBIT(BITree, n, index, val):
    index += 1
    while index <= n:
        BITree[index] += val
        index += index & (-index)


def constructBITree(arr, n):
    BITree = [0] * (n + 1)
    for i in xrange(0, n):
        updateBIT(BITree, n, i, arr[i])
    return BITree


def getSum(BITree, index):
    sum = 0
    index += 1
    while index > 0:
        sum += BITree[index]
        sum %= 1000000007
        index -= index & (-index)
    return sum


def update(BITree, l, r, n, val):
    updateBIT(BITree, n, l, val)
    updateBIT(BITree, n, r + 1, -val)


def queried(query, index):
    if query[0] == 1:
        mapper[index] += 1
        mapper[index] %= 1000000007
    else:
        for k in xrange(query[1] - 1, query[2]):
            queried(queries[k], k)

n = input()
for x in xrange(0, n):
    n, m = map(int, raw_input().split())
    array = [0] * n
    BITree = constructBITree(array, n)
    queries = []
    mapper = [0] * m
    for p in xrange(0, m):
        queries.append(map(int, raw_input().strip().split()))
    for i in xrange(0, m):
        queried(queries[i], i)
    for i in xrange(0, m):
        if mapper[i] > 0:
            update(BITree, queries[i][1] - 1, queries[i][2] - 1, n, mapper[i])
    for i in xrange(0, n):
        print getSum(BITree, i),
    print
