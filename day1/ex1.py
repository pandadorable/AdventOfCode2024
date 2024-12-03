import re
t = open("input.txt")
L = []
R = []
for l in t.readlines():
    l,r = list(map(int, re.findall(r'\d+', l)))
    L.append(l)
    R.append(r)
L.sort()
R.sort()
s = 0
for i in range(len(L)):
    s += abs(L[i]-R[i])
print(s)