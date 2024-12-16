import sys
sys.setrecursionlimit(10000)


input = open("./day12/input.txt")
GRID = [list(l.strip('\n')) for l in input.readlines()]
isVerifGRID = [[False for _ in range(len(GRID[i]))] for i in range(len(GRID))]

def isValidPos(i,j):
    return i >= 0 and i < len(GRID) and j >=0 and j < len(GRID[i])

def recurField(crop,i,j):
    nbSubCrop = 1
    listSub = [[i,j]]
    isVerifGRID[i][j] = True
    
    for x,y in [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]:
        if isValidPos(x,y) and GRID[x][y] == crop and not isVerifGRID[x][y]:
            cr,br = recurField(crop,x,y)
            nbSubCrop += cr
            listSub += br
    
    return nbSubCrop,listSub
            

def validateField(i,j):
    if not isVerifGRID[i][j]:
        area,listSub = recurField(GRID[i][j],i,j)
        
        GRID_FORM = [['.' for _ in range(len(GRID[0]))] for _ in range(len(GRID))]
        for i,j in listSub:
            GRID_FORM[i][j] = 'X'
        
        GRID_TEST = [['.' for _ in range(len(GRID[0])*3)] for _ in range(len(GRID)*3)]
        for i,j in listSub:
            a,b = 3*i+1,3*j+1
            GRID_TEST[a][b] = 'X'
            for x,y in [[-1,0],[1,0],[0,-1],[0,1]]:
                if i+x >= 0 and i+x < len(GRID_FORM) and j+y >= 0 and j+y < len(GRID_FORM[0]):
                    if GRID_FORM[i+x][j+y] == 'X':
                        GRID_TEST[a+x][b+y] = 'X'
                    else:
                        GRID_TEST[a+x][b+y] = '+'
                else:
                    GRID_TEST[a+x][b+y] = '+'    
            for x,y in [[-1,-1],[1,-1],[-1,1],[1,1]]:
                if i+x >= 0 and i+x < len(GRID_FORM) and j+y >= 0 and j+y < len(GRID_FORM[0]):
                    if GRID_FORM[i+x][j+y] == 'X' and GRID_FORM[i+x][j] == 'X' and GRID_FORM[i][j+y] == 'X':
                        GRID_TEST[a+x][b+y] = 'X'
                    else:
                        GRID_TEST[a+x][b+y] = '+'
                else:
                    GRID_TEST[a+x][b+y] = '+'        
                        
        for i in range(len(GRID_TEST)):
            for j in range(len(GRID_TEST[0])):
                if GRID_TEST[i][j] == '+':
                    if not ((i == 0 or i == len(GRID_TEST)-1) and (j == 0 or j == len(GRID_TEST[0])-1)):
                        if i == 0 or i == len(GRID_TEST)-1:
                            if GRID_TEST[i][j-1] in ['+','-'] and GRID_TEST[i][j+1] in ['+','-']:
                                GRID_TEST[i][j] = '-'
                        elif j == 0 or j == len(GRID_TEST[0])-1:
                            if GRID_TEST[i-1][j] in ['+','-'] and GRID_TEST[i+1][j] in ['+','-']:
                                GRID_TEST[i][j] = '-'
                        elif (GRID_TEST[i][j-1] in ['+','-'] and GRID_TEST[i][j+1] in ['+','-']) or (GRID_TEST[i-1][j] in ['+','-'] and GRID_TEST[i+1][j] in ['+','-']):
                            GRID_TEST[i][j] = '-'                
        nbSommet = 0
        for i in GRID_TEST:
            #print(''.join(i))
            nbSommet += i.count('+')
        #print()
        return area,nbSommet
    return 0,0

sum = 0
for i in range(len(GRID)):
    for j in range(len(GRID[i])):
        area,perimeter = validateField(i,j)
        sum += area*perimeter
print(sum)