input = open("./day10/input.txt")
GRID = [list(map(int,l.strip('\n'))) for l in input.readlines()]

def isValid(pos):
    return pos[0] >=0 and pos[0] < len(GRID) and pos[1] >= 0 and pos[1] < len(GRID[0])

def recur(pos):
    val = GRID[pos[0]][pos[1]]
    #print(val)
    if val == 9:
        return [pos]
    
    listPos = []
    if isValid([pos[0]-1,pos[1]]) and GRID[pos[0]-1][pos[1]] == val+1:
        listPos += recur([pos[0]-1,pos[1]])
    if isValid([pos[0]+1,pos[1]]) and GRID[pos[0]+1][pos[1]] == val+1:
        listPos += recur([pos[0]+1,pos[1]])
    if isValid([pos[0],pos[1]-1]) and GRID[pos[0]][pos[1]-1] == val+1:
        listPos += recur([pos[0],pos[1]-1])
    if isValid([pos[0],pos[1]+1]) and GRID[pos[0]][pos[1]+1] == val+1:
        listPos += recur([pos[0],pos[1]+1])
    return listPos

def countUnique(list):
    newList = []
    for v in list:
        if v not in newList:
            newList.append(v)
    return len(newList)


sum = 0
for i in range(len(GRID)):
    for j in range(len(GRID[0])):
        if GRID[i][j] == 0:
            sum += countUnique(recur([i,j]))
print(sum)
