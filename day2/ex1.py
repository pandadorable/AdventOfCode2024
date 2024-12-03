import re
from functools import reduce
from operator import mul
t = open("input.txt")
safe = 0
for l in t.readlines():
    report = list(map(int, re.findall(r'\d+', l)))
    steps = [report[i]-report[i+1] for i in range(len(report)-1)]
    maxVal = max(steps,key=abs)
    if(abs(maxVal) < 4 and (all(item >= 0 for item in steps) or all(item < 0 for item in steps)) and 0 not in steps):
        safe += 1
        print(steps)
        print(abs(maxVal))
    
print(safe)
        