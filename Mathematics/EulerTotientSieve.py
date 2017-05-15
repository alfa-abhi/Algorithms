maxn = 1000001
phi = [0] * maxn
phi[1] = 1
prime = [0] * (maxn/10)
mark = [False] * maxn
sz = 0
for i in xrange(2, maxn):
    if not mark[i]:
        phi[i] = i -1
        prime[sz] = i
        sz += 1
    j = 0
    while j < sz and prime[j] * i < maxn:
        mark[prime[j] * i] = True
        if i % prime[j] == 0:
            ll = 0
            xx = i
            while xx % prime[j] == 0:
                xx /= prime[j]
                ll += 1
            mm = 1
            for k in xrange(0, ll):
                mm *= prime[j]
            phi[i * prime[j]] = phi[xx] * mm * (prime[j] - 1)
            break
        else:
            phi[i * prime[j]] = phi[i] * (prime[j] - 1)
        j += 1