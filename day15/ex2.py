input = open("./day15/input.txt")
GRID = []
for l in input:
    if l == '\n':
        break
    line = []
    for case in list(l.strip('\n')):
        match(case):
            case '#':
                line += list("##")
            case 'O':
                line += list("[]")
            case '.':
                line += list("..")
            case '@':
                line += list("@.")
    GRID.append(line)

commandList = []
 
for l in input:
    commandList += list(l.strip('\n'))
    


robotPos = ()
for i in range(len(GRID)):
    for j in range(len(GRID[0])):
        if GRID[i][j] == '@':
            robotPos = (i,j)


LIST_TO_MOVE = []

def canPushBox(pos,dir):
    
    if GRID[pos[0]][pos[1]] == '#':
        return False
    if GRID[pos[0]][pos[1]] == '.':
        return True
    
    nextPos = (pos[0] + dir[0],pos[1] + dir[1])
    if dir[0] == 0:
        if canPushBox(nextPos,dir):
            return True
    elif dir[1] == 0:
        if GRID[pos[0]][pos[1]] == ']':
            otherNext = (nextPos[0],nextPos[1]-1)
            if canPushBox(nextPos,dir) and canPushBox(otherNext,dir):
                return True
        elif GRID[pos[0]][pos[1]] == '[':
            otherNext = (nextPos[0],nextPos[1]+1)
            if canPushBox(nextPos,dir) and canPushBox(otherNext,dir):
                return True
    return False

def pushBox(pos,dir):
    
    if GRID[pos[0]][pos[1]] == '#':
        return False
    if GRID[pos[0]][pos[1]] == '.':
        return True
    
    nextPos = (pos[0] + dir[0],pos[1] + dir[1])
    if dir[0] == 0:
        if pushBox(nextPos,dir):
            GRID[pos[0]+dir[0]][pos[1]+dir[1]] = GRID[pos[0]][pos[1]]
            GRID[pos[0]][pos[1]] = '.'
            return True
    elif dir[1] == 0:
        if GRID[pos[0]][pos[1]] == ']':
            otherNext = (nextPos[0],nextPos[1]-1)
            if pushBox(nextPos,dir) and pushBox(otherNext,dir):
                GRID[pos[0]+dir[0]][pos[1]] = GRID[pos[0]][pos[1]]
                GRID[pos[0]+dir[0]][pos[1]-1] = GRID[pos[0]][pos[1]-1]
                GRID[pos[0]][pos[1]] = '.'
                GRID[pos[0]][pos[1]-1] = '.'
                return True
        elif GRID[pos[0]][pos[1]] == '[':
            otherNext = (nextPos[0],nextPos[1]+1)
            if pushBox(nextPos,dir) and pushBox(otherNext,dir):
                GRID[pos[0]+dir[0]][pos[1]] = GRID[pos[0]][pos[1]]
                GRID[pos[0]+dir[0]][pos[1]+1] = GRID[pos[0]][pos[1]+1]
                GRID[pos[0]][pos[1]] = '.'
                GRID[pos[0]][pos[1]+1] = '.'
                return True
    return False
                

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
    if canPushBox((robotPos[0]+dir[0],robotPos[1]+dir[1]),dir):
        pushBox((robotPos[0]+dir[0],robotPos[1]+dir[1]),dir)
        GRID[robotPos[0]][robotPos[1]] = '.'
        robotPos = (robotPos[0] + dir[0],robotPos[1] + dir[1])
        GRID[robotPos[0]][robotPos[1]] = '@'
    # else:
    #     print(c,robotPos)
    #     for i in GRID:
    #         print(''.join(i))

for i in GRID:
    print(''.join(i))
    
sum = 0
for i in range(len(GRID)):
    for j in range(len(GRID[0])):
        if GRID[i][j] == '[':
            sum += 100*i+j
                        
print(sum)