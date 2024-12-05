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
        
def isBreakingLaw(l,i):
    for x in range(i+1,len(l)):
        if l[i] in ALL_PREVIOUS.keys() and l[x] in ALL_PREVIOUS[l[i]]:
            return True
    return False

sum_middle_page = 0

for u in input.readlines():
    l = list(map(int,u.strip('\n').split(',')))
    for i in range(len(l)):
        if isBreakingLaw(l,i):
            break
        elif l[i] == l[-1]:
            sum_middle_page += l[(len(l) - 1)//2]
            
print(sum_middle_page)