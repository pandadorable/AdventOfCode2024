import sys
import math
sys.setrecursionlimit(10000)

input = open("./day16/input.txt")
GRID = []
for l in input:
    GRID.append(list(l.strip('\n')))
BEST_VALUE = [[-1 for _ in range(len(GRID[0]))] for _ in range(len(GRID))]
    

pos = [0,0]
for i in range(len(GRID)):
    for j in range(len(GRID[0])):
        if GRID[i][j] == 'E':
            pos = [i,j]
start = [0,0]
for i in range(len(GRID)):
    for j in range(len(GRID[0])):
        if GRID[i][j] == 'S':
            start = [i,j]
            
def findBestPath(pos,dir,val):
    if GRID[pos[0]][pos[1]] != '#':
        if BEST_VALUE[pos[0]][pos[1]] > val or BEST_VALUE[pos[0]][pos[1]] == -1:
            BEST_VALUE[pos[0]][pos[1]] = val
            
            if GRID[pos[0]][pos[1]] == 'E':
                return

            findBestPath([pos[0]+dir[0],pos[1]+dir[1]],dir,val+1)
            findBestPath([pos[0]-dir[1],pos[1]+dir[0]],[-dir[1],dir[0]],val+1001)
            findBestPath([pos[0]+dir[1],pos[1]-dir[0]],[dir[1],-dir[0]],val+1001)
            

def drawPaths(pos):
    if GRID[pos[0]][pos[1]] in ['.','E','S']:
        GRID[pos[0]][pos[1]] = 'O'
        
        if BEST_VALUE[pos[0]][pos[1]] - BEST_VALUE[pos[0]][pos[1]-1] in [1,1001]:
            drawPaths([pos[0],pos[1]-1])
        if BEST_VALUE[pos[0]][pos[1]] - BEST_VALUE[pos[0]][pos[1]+1] in [1,1001]:
            drawPaths([pos[0],pos[1]+1])
        if BEST_VALUE[pos[0]][pos[1]] - BEST_VALUE[pos[0]-1][pos[1]] in [1,1001]:
            drawPaths([pos[0]-1,pos[1]])
        if BEST_VALUE[pos[0]][pos[1]] - BEST_VALUE[pos[0]+1][pos[1]] in [1,1001]:
            drawPaths([pos[0]+1,pos[1]])
            

findBestPath(start,[0,1],0)
for i in BEST_VALUE:
        print('\t'.join(map(str,i)))
print(BEST_VALUE[pos[0]][pos[1]])

drawPaths(pos)

for l in GRID:
    print(''.join(l))