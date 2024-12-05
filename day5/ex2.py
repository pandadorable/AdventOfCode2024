input = open("./day5/input.txt")
ALL_PREVIOUS = {}
l = input.readline()
while l != '\n':
    a,b = list(map(int,l.strip('\n').split('|')))
    if b not in ALL_PREVIOUS.keys():
        ALL_PREVIOUS[b] = [a]
    else:
        ALL_PREVIOUS[b].append(a)
    l = input.readline()
        
def isBreakingLaw(l):
    for i in range(len(l)):
        for x in range(i+1,len(l)):
            if l[i] in ALL_PREVIOUS.keys() and l[x] in ALL_PREVIOUS[l[i]]:
                return True
    return False

def FixingLaw(l):
    j = 0
    while j < len(l):
        print('start',l)
        print('j-',j)
        for x in range(j+1,len(l)):
            print('x-',x)
            if l[j] in ALL_PREVIOUS.keys() and l[x] in ALL_PREVIOUS[l[j]]:
                badVal = l.pop(x)
                l.insert(j,badVal)
                j = -1
                break
        print('loop',l)
        j += 1
    print('fixed',l)
    return l[(len(l)-1)//2]

sum_middle_page = 0

for u in input.readlines():
    l = list(map(int,u.strip('\n').split(',')))
    if isBreakingLaw(l):
        print('bad',l)
        sum_middle_page += FixingLaw(l)
    else:
        print('good',l)
            
print(sum_middle_page)