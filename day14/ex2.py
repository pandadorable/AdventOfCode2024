import numpy
from PIL import Image
import PIL

input = open("./day14/input.txt")
GRID = [['.' for _ in range(101)] for _ in range(103)]
class robot:
    pos = (0,0)
    dir = (0,0)
    def __init__(self,pos,dir):
        self.pos = pos
        self.pos[0],self.pos[1] = self.pos[1],self.pos[0]
        self.dir = dir
        self.dir[0],self.dir[1] = self.dir[1],self.dir[0]
        print(self.pos,self.dir)
    
    def update(self):
        #print(self.dir,self.pos,end='')
        self.pos[0] = (self.pos[0]+self.dir[0])%len(GRID)
        self.pos[1] = (self.pos[1]+self.dir[1])%len(GRID[0])
        #print(self.pos)

listR = []
for l in input.readlines():
    p,d = l.strip('\n').split()
    p = p.split("=")
    pos = list(map(int,p[1].split(',')))
    d = d.split("=")
    dir = list(map(int,d[1].split(',')))
    listR.append(robot(pos,dir))
    
for r in listR:
    p = r.pos
    print(p)
    if GRID[p[0]][p[1]] == '.':
        GRID[p[0]][p[1]] = 1
    else:
        GRID[p[0]][p[1]] += 1
# for i in range(len(GRID)):
#     for j in range(len(GRID[0])):
#         print(GRID[i][j],end='')
#     print()
# print()
    
for loop in range(10000):
    data = numpy.zeros((103, 101, 3), dtype=numpy.uint8)
    GRID = [['.' for _ in range(len(GRID[0]))] for _ in range(len(GRID))]
    for r in listR:
        r.update()
        p = r.pos
        if GRID[p[0]][p[1]] == '.':
            GRID[p[0]][p[1]] = 1
        else:
            GRID[p[0]][p[1]] += 1
    for i in range(len(GRID)):
        for j in range(len(GRID[0])):
            if GRID[i][j] != '.':
                data[i,j] = [255,255,255]
    image = Image.fromarray(data)
    image.save("./day14/output/"+str(loop)+".png")