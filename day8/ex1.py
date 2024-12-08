input = open("./day8/input.txt")
ANTENNA = {}
GRID = [list(l.strip('\n')) for l in input.readlines()]
for i in range(len(GRID)):
    for j in range(len(GRID[i])):
        if GRID[i][j] != '.':
            if GRID[i][j] not in ANTENNA.keys():
                ANTENNA[GRID[i][j]] = []
            ANTENNA[GRID[i][j]].append([i,j])

for k,v in ANTENNA.items():
    print(k)
    for a in v:
        for b in v:
            if a != b :
                pos = [a[0]-(b[0]-a[0]),a[1]-(b[1]-a[1])]
                if pos[0] >= 0 and pos[0] < len(GRID) and pos[1] >=0 and pos[1] < len(GRID[0]):
                    GRID[pos[0]][pos[1]] = '#'
                    
sum = 0
for i in GRID:
    print(''.join(i))
    sum += i.count('#')
print(sum)
