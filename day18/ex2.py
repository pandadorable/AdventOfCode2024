import re
import sys

sys.setrecursionlimit(10000)

input = open("./day18/input.txt")
GRID_SIZE = 71
GRID = [[ 0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
DIST = [[ GRID_SIZE*GRID_SIZE for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
PATH = [[ '.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
last_pos = []
k = 0

def addLine():
    global GRID_SIZE, GRID, DIST, PATH, last_pos, k, input
    k += 1
    i,j = list(map(int, re.findall(r'\d+', input.readline())))
    last_pos = [i,j]
    GRID[j][i] = k
    return PATH[j][i] == 'O'

def recur(pos,val):
    global GRID_SIZE, GRID, DIST, PATH
    if pos[0] >= 0 and pos[0] < GRID_SIZE and pos[1] >= 0 and pos[1] < GRID_SIZE:
        if GRID[pos[0]][pos[1]] == 0:
            if DIST[pos[0]][pos[1]] > val:
                DIST[pos[0]][pos[1]] = val
                recur([pos[0]+1,pos[1]],val+1)
                recur([pos[0]-1,pos[1]],val+1)
                recur([pos[0],pos[1]+1],val+1)
                recur([pos[0],pos[1]-1],val+1)

def fillPath(pos):
    global GRID_SIZE, GRID, DIST, PATH
    PATH[pos[0]][pos[1]] = 'O'
    for i,j in [[pos[0]-1,pos[1]],[pos[0]+1,pos[1]],[pos[0],pos[1]-1],[pos[0],pos[1]+1]]:
        if i >= 0 and i < GRID_SIZE and j >= 0 and j < GRID_SIZE and DIST[i][j] == DIST[pos[0]][pos[1]]-1:
            fillPath([i,j])
            break



for _ in range(2048):
    addLine()

recur([0,0],1)
fillPath([GRID_SIZE-1,GRID_SIZE-1])

while DIST[-1][-1] != GRID_SIZE*GRID_SIZE:
    while addLine():
        print(last_pos)
    DIST = [[ GRID_SIZE*GRID_SIZE for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    PATH = [[ '.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    recur([0,0],1)
    fillPath([GRID_SIZE-1,GRID_SIZE-1])
    

    # for i in GRID:
    #     print('\t'.join(list(map(str,i))))   
    # print()  
    # for i in DIST:
    #     print('\t'.join(list(map(str,i))))    
    # print()
    # for i in PATH:
    #     print('\t'.join(i))
    #print("\n\n")