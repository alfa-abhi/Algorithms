string1 = list(raw_input().lower())
string2 = list(raw_input().lower())
counter1 = {}
counter2 = {}
for i in string1:
    counter1[i] = 0

for i in string2:
    counter2[i] = 0

for i in string1:
    counter1[i] += 1

for i in string2:
    counter2[i] += 1

flag = False
if len(set(string1) - set(string2)) == 0 and len(set(string2) - set(string1)) == 0:
    for k in set(string1):
        if counter1[k] != counter2[k]:
            flag = True
            break
else:
    flag = True

if flag:
    print "Not an Anagram"
else:
    print "Anagram"
