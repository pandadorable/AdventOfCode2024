input = open("./day6/input.txt")
GRID = [list(l.strip('\n')) for l in input.readlines()]
pos = []
dir = [-1,0]
for i in range(len(GRID)):
    if '^' in GRID[i]:
        pos.append(i)
        pos.append(GRID[i].index('^'))
    
while(True):
    next_bloc = [pos[0]+dir[0],pos[1]+dir[1]]
    GRID[pos[0]][pos[1]] = 'X'
    if next_bloc[0] < 0 or next_bloc[0] > len(GRID)-1 or next_bloc[1] < 0 or next_bloc[1] > len(GRID[0])-1:
        break
    elif GRID[next_bloc[0]][next_bloc[1]] == '#':
        dir = [dir[1],-dir[0]]
    else:
        pos = next_bloc

s = 0
for i in GRID:
    s += i.count('X')
    print(''.join(i))
print(s)