def getGrid():
    return [list(l.strip('\n')) for l in open("./day6/input.txt").readlines()]


PATH_GRID = getGrid()
pos = []
dir = [-1,0]
for i in range(len(PATH_GRID)):
    if '^' in PATH_GRID[i]:
        pos.append(i)
        pos.append(PATH_GRID[i].index('^'))

while(True):
    next_bloc = [pos[0]+dir[0],pos[1]+dir[1]]
    PATH_GRID[pos[0]][pos[1]] = 'X'
    if next_bloc[0] < 0 or next_bloc[0] > len(PATH_GRID)-1 or next_bloc[1] < 0 or next_bloc[1] > len(PATH_GRID[0])-1:
        break
    elif PATH_GRID[next_bloc[0]][next_bloc[1]] == '#':
        dir = [dir[1],-dir[0]]
    else:
        pos = next_bloc


def isLooping(GRID,pos_obs):
    DIR_GRID = [[[] for _ in range(len(GRID[0]))] for _ in range(len(GRID))]
    
    start_pos = []
    start_dir = [-1,0]
    for i in range(len(GRID)):
        if '^' in GRID[i]:
            start_pos.append(i)
            start_pos.append(GRID[i].index('^'))
    GRID[pos_obs[0]][pos_obs[1]] = 'O'
    while(True):
        next_bloc = [start_pos[0]+start_dir[0],start_pos[1]+start_dir[1]]
        
        match start_dir:
            case [-1,0]:
                if 'UP' in DIR_GRID[start_pos[0]][start_pos[1]]:
                    return True
                DIR_GRID[start_pos[0]][start_pos[1]].append('UP')
            case [1,0]:
                if 'DOWN' in DIR_GRID[start_pos[0]][start_pos[1]]:
                    return True
                DIR_GRID[start_pos[0]][start_pos[1]].append('DOWN')
            case [0,-1]:
                if 'LEFT' in DIR_GRID[start_pos[0]][start_pos[1]]:
                    return True
                DIR_GRID[start_pos[0]][start_pos[1]].append('LEFT')
            case [0,1]:
                if 'RIGHT' in DIR_GRID[start_pos[0]][start_pos[1]]:
                    return True
                DIR_GRID[start_pos[0]][start_pos[1]].append('RIGHT')
        
        if next_bloc[0] < 0 or next_bloc[0] > len(GRID)-1 or next_bloc[1] < 0 or next_bloc[1] > len(GRID[0])-1:
            break
        elif GRID[next_bloc[0]][next_bloc[1]] in ['#','O']:
            start_dir = [start_dir[1],-start_dir[0]]
        else:
            start_pos = next_bloc
    return False

s = 0
for i in PATH_GRID:
    s += i.count('X')
print('nb step',s)

nb_loop = 0
for i in range(len(PATH_GRID)):
    for j in range(len(PATH_GRID[0])):
        if PATH_GRID[i][j] == 'X':
            print('[',s,']',i,j)
            if isLooping(getGrid(),[i,j]):
                nb_loop += 1
            s-=1
print(nb_loop)