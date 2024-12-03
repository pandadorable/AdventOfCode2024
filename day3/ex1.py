import re
t = open("input.txt").read()
l = re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)", t)
s = 0
for m in l:
    a,b = list(map(int, re.findall(r'\d+', m)))
    s+= a*b
print(s)