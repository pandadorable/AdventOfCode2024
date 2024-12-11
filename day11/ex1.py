pre_list_stone = list(map(int,open("./day11/input.txt").readline().strip('\n').split()))
for i in range(25):
    next_list = []
    for rock in pre_list_stone:
        if rock == 0:
            next_list.append(1)
        elif len(str(rock))%2 == 0:
            str_rock = str(rock)
            r1,r2 = str_rock[:len(str_rock)//2], str_rock[len(str_rock)//2:]
            next_list.append(int(r1))
            next_list.append(int(r2))
        else:
            next_list.append(rock*2024)
    #print('[',i,']',next_list)
    pre_list_stone = next_list
print(len(pre_list_stone))