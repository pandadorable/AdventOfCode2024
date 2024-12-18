import re
import sys

sys.setrecursionlimit(10000)

GRID_SIZE = 7
GRID = [[ 0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
DIST = [[ GRID_SIZE*GRID_SIZE for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


k = 1
input = open("./day18/input.txt")
for l in range(12):
    i,j = list(map(int, re.findall(r'\d+', input.readline())))
    GRID[j][i] = k
    k += 1

def recur(pos,val):
    if pos[0] >= 0 and pos[0] < GRID_SIZE and pos[1] >= 0 and pos[1] < GRID_SIZE:
        if GRID[pos[0]][pos[1]] == 0:
            if DIST[pos[0]][pos[1]] > val:
                DIST[pos[0]][pos[1]] = val
                recur([pos[0]+1,pos[1]],val+1)
                recur([pos[0]-1,pos[1]],val+1)
                recur([pos[0],pos[1]+1],val+1)
                recur([pos[0],pos[1]-1],val+1)

recur([0,0],1)

for i in GRID:
    print('\t'.join(list(map(str,i))))   
print()  
for i in DIST:
    print('\t'.join(list(map(str,i))))
print(DIST[-1][-1]-1)