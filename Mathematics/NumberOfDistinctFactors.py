sieve = [True] * 100000
sieve[0] = False
sieve[1] = False
for x in xrange(2, 100000):
    if sieve[x]:
        for k in xrange(x+x, 100000, x):
            sieve[k] = False

n = input()
divisors = 1
count = 0
while n % 2 == 0:
    count += 1
    n /= 2
divisors *= count + 1
for x in xrange(3, 100000):
    count = 0
    if sieve[x]:
        while n % x == 0:
            count += 1
            n /= x
        divisors *= count + 1

print divisors
