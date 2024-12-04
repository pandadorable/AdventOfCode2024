input = open("./day4/input.txt")
TAB = []
for l in input.readlines():
    TAB.append(['.','.','.','.']+list(l.strip('\n'))+['.','.','.','.'])
pLine = ['.' for i in range(len(TAB[0]))]
for i in range(4):
    TAB.insert(0,pLine)
for i in range(4):
    TAB.append(pLine)
    
XMAS = ['M.M\n.A.\nS.S','M.S\n.A.\nM.S','S.M\n.A.\nS.M','S.S\n.A.\nM.M']

def verifCrossMass(i,j):
    s = TAB[i-1][j-1]+'.'+TAB[i-1][j+1]+'\n'+'.'+TAB[i][j]+'.'+'\n'+TAB[i+1][j-1]+'.'+TAB[i+1][j+1]
    #print(s)
    return s in XMAS

s = 0  
for i in range(4,len(TAB)-4):
    for j in range(4,len(TAB)-4):
        if verifCrossMass(i,j):
            s += 1
print(s)