input = open("./day15/input.txt")
GRID = []
for l in input:
    if l == '\n':
        break
    GRID.append(list(l.strip('\n')))

commandList = []
 
for l in input:
    commandList += list(l.strip('\n'))


robotPos = ()
for i in range(len(GRID)):
    for j in range(len(GRID[0])):
        if GRID[i][j] == '@':
            robotPos = (i,j)

def pushBox(pos,dir):
    
    if GRID[pos[0]][pos[1]] == '#':
        return False
    if GRID[pos[0]][pos[1]] == '.':
        return True
    
    nextPos = (pos[0] + dir[0],pos[1] + dir[1])
    if pushBox(nextPos,dir):
        GRID[pos[0]][pos[1]] = '.'
        GRID[pos[0]+dir[0]][pos[1]+dir[1]] = 'O'
        return True

for c in commandList:
    dir = ()
    match c:
        case '<':
            dir = (0,-1)
        case '>':
            dir = (0,1)
        case '^':
            dir = (-1,0)
        case 'v':
            dir = (1,0)
    if pushBox((robotPos[0]+dir[0],robotPos[1]+dir[1]),dir):
        GRID[robotPos[0]][robotPos[1]] = '.'
        robotPos = (robotPos[0] + dir[0],robotPos[1] + dir[1])
        GRID[robotPos[0]][robotPos[1]] = '@'

for i in GRID:
    print(''.join(i))
    
    
sum = 0
for i in range(len(GRID)):
    for j in range(len(GRID[0])):
        if GRID[i][j] == 'O':
            sum += 100*i+j
                        
print(sum)