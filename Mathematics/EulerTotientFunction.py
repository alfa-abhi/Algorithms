def phi(n):
    res = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n /= p
            res -= res / p
        p += 1
    if n > 1:
        res -= res / n
    return res

for x in xrange(1, 11):
    print phi(x)
