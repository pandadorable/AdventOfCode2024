from functools import *
CACHE = {}

@cache
def check(rock):
    list = []
    if rock == 0:
        return [1]
    elif len(str(rock))%2 == 0:
        str_rock = str(rock)
        r1,r2 = str_rock[:len(str_rock)//2], str_rock[len(str_rock)//2:]
        return [int(r1),int(r2)]
    else:
        return [rock*2024]

pre_list_stone = list(map(int,open("./day11/input.txt").readline().strip('\n').split()))
pre_dict = {}
for i in pre_list_stone:
    if i not in pre_dict.keys():
        pre_dict[i] = 1
    else:
        pre_dict[i] += 1


for i in range(75):
    next_dict = {}
    for rock in pre_dict.keys():
        for val in check(rock):
            if val not in next_dict.keys():
                next_dict[val] = pre_dict[rock]
            else:
                next_dict[val] += pre_dict[rock]
    print('[',i,']')
    pre_dict = next_dict


sum = 0
for _,v in pre_dict.items():
    sum += v
print(sum)
