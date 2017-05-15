acts_in_pool = input()
activities = []
for x in xrange(0, acts_in_pool):
    st_end = map(int, raw_input().split())
    activities.append(st_end)
activities.sort(key=lambda y: y[1])
sel_acts = [1]
end = activities[0][1]
for i in xrange(1, acts_in_pool):
    if activities[i][0] >= end:
        sel_acts.append(i+1)
        end = activities[i][1]
print(sel_acts)