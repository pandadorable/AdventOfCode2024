import re
from functools import reduce
from operator import mul
t = open("message.txt")
safe = 0

def isGoodRepport(report):
    steps = [report[i]-report[i+1] for i in range(len(report)-1)]
    maxVal = max(steps,key=abs)
    return abs(maxVal) < 4 and (all(item > 0 for item in steps) or all(item < 0 for item in steps)) and 0 not in steps



for l in t.readlines():
    report = list(map(int, re.findall(r'\d+', l)))
    isSafe = isGoodRepport(report)
    if not isSafe:
        for i in range(len(report)):
            subReport = report.copy()
            del subReport[i]
            isSafe = isGoodRepport(subReport)
            if isSafe:
                break
    if isSafe:
        safe += 1
        
print(safe)
        