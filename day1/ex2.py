import re
t = open("input.txt")
L = {}
R = {}
for l in t.readlines():
    l,r = list(map(int, re.findall(r'\d+', l)))
    if l not in L.keys():
        L[l] = 0
    if r not in R.keys():
        R[r] = 0
    L[l] += 1
    R[r] += 1
s = 0
for v in L.keys():
    if v in R.keys():
        s += v*R[v]
print(s)