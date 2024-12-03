import re
t = "do()"+open("input.txt").read()
doBalise = re.finditer(r"do\(\)", t)
dontBalise = re.finditer(r"don\'t\(\)", t)
doList = []
dontList = []
for doMatch in doBalise:
    doList.append(doMatch.start())
for dontMatch in dontBalise:
    dontList.append(dontMatch.start())
interval = []
while(len(doList) > 0 and len(dontList) > 0):
    min = doList.pop(0)
    while(len(dontList) > 0 and dontList[0] < min):
        dontList.pop(0)
    max = dontList.pop(0)
    while(len(doList) > 0 and doList[0] < max):
        doList.pop(0)
    interval.append([min,max])
print(interval)
s = 0
for i in interval:
    l = re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)", t[i[0]:i[1]])
    for m in l:
        a,b = list(map(int, re.findall(r'\d+', m)))
        s+= a*b
print(s)