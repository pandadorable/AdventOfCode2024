input = open("./day4/input.txt")
TAB = []
for l in input.readlines():
    TAB.append(['.','.','.','.']+list(l.strip('\n'))+['.','.','.','.'])
pLine = ['.' for i in range(len(TAB[0]))]
for i in range(4):
    TAB.insert(0,pLine)
for i in range(4):
    TAB.append(pLine)

def countXmasFromx(i,j):
    l = []
    l.append(''.join([TAB[i-x][j] for x in range(4)]))
    l.append(''.join([TAB[i+x][j] for x in range(4)]))
    l.append(''.join([TAB[i][j-x] for x in range(4)]))
    l.append(''.join([TAB[i][j+x] for x in range(4)]))
    l.append(''.join([TAB[i-x][j-x] for x in range(4)]))
    l.append(''.join([TAB[i+x][j+x] for x in range(4)]))
    l.append(''.join([TAB[i-x][j+x] for x in range(4)]))
    l.append(''.join([TAB[i+x][j-x] for x in range(4)]))
    return l.count('XMAS')

s = 0  
for i in range(4,len(TAB)-4):
    for j in range(4,len(TAB)-4):
        s += countXmasFromx(i,j)
print(s)