from math import sqrt


line = map(int, raw_input().split())  # x1 y1 x2 y2
radius = input()  # circle radius
a = line[1] - line[3]
b = line[2] - line[0]
c = abs(((line[0] - line[2]) * line[1]) + ((line[3] - line[1]) * line[2]))
answer = c / sqrt(a*a + b*b)
if answer < radius:
    print "Intersecting"
elif answer == radius:
    print "Tangent"
else:
    print "Non Touching"
