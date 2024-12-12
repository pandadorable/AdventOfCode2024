import sys
sys.setrecursionlimit(10000)


input = open("./day12/input.txt")
GRID = [list(l.strip('\n')) for l in input.readlines()]
isVerifGRID = [[False for _ in range(len(GRID[i]))] for i in range(len(GRID))]

def isValidPos(i,j):
    return i >= 0 and i < len(GRID) and j >=0 and j < len(GRID[i])

def recurField(crop,i,j):
    nbSubCrop = 1
    nbBarrier = 0
    isVerifGRID[i][j] = True
    
    for x,y in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
        if isValidPos(x,y):
            if GRID[x][y] != crop:
                nbBarrier +=1
            elif not isVerifGRID[x][y]:
                cr,br = recurField(crop,x,y)
                nbSubCrop += cr
                nbBarrier += br
        else:
            nbBarrier += 1
    
    return nbSubCrop,nbBarrier
            

def validateField(i,j):
    if not isVerifGRID[i][j]:
        area,perimeter = recurField(GRID[i][j],i,j)
        return area,perimeter
    return 0,0

sum = 0
for i in range(len(GRID)):
    for j in range(len(GRID[i])):
        area,perimeter = validateField(i,j)
        sum += area*perimeter
print(sum)