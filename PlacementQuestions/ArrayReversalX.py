# O(n) solution for reversing a section an array.

array = map(int, raw_input().split())
x = input() - 1
k = 0
counter = (x - k) / 2
p = 0
while counter > 0:
    array[x], array[k] = array[k], array[x]
    x -= 1
    k += 1
    counter -= 1
    print array
