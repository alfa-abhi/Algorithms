sieve = [True] * 100000
sieve[0] = False
sieve[1] = False
for x in xrange(2, 100000):
    if sieve[x]:
        for k in xrange(x+x, 100000, x):
            sieve[k] = False

print sieve
