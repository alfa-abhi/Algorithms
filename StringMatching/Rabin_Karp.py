import math

d = 256
def search(pattern, text, prime_number):
    m = len(pattern)
    n = len(text)
    j = 0
    p = 0
    t = 0
    h = pow(d, m-1, prime_number)
    # print h
    for i in xrange(m):
        p = (d*p + ord(pattern[i])) % prime_number
        t = (d*t + ord(text[i])) % prime_number
    # print(p, t)
    for i in xrange(n-m+1):
        if p == t:
            for j in xrange(m):
                if text[i+j] != pattern[j]:
                    break
            j += 1
            if j == m:
                print "Pattern Found at " + str(i)

        if i < n-m:
            t = (d*(t - ord(text[i])*h) + ord(text[i+m])) % prime_number
            # print t
            if t < 0:
                t = t + prime_number

tex = raw_input()
pat = raw_input()
prime = 101
search(pat, tex, prime)
