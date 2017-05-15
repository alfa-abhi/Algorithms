number = input()
binary = []
while number > 0:
    binary.append(number % 2)
    number /= 2
binary.reverse()
length = len(binary)
mid = length / 2
k = 0
flag = True
while k <= mid:
    if binary[k] != binary[length - k - 1]:
        flag = False
        print "Not Palindrome"
        break
    k += 1
if flag:
    print "Palindrome"
