import math
input = open("./day13/input.txt")

def _1game():
    bpA = input.readline().strip('\n').split()
    bpA = [bpA[i] for i in range(2,4)]
    bpA = list(map(int,[bpA[i].split("+")[1].strip(',') for i in range(2)]))
    bpB = input.readline().strip('\n').split()
    bpB = [bpB[i] for i in range(2,4)]
    bpB = list(map(int,[bpB[i].split("+")[1].strip(',') for i in range(2)]))
    goal = input.readline().strip('\n').split()
    goal = [goal[i] for i in range(1,3)]
    goal = list(map(int,[goal[i].split("=")[1].strip(',') for i in range(2)]))
    #print(bpA,bpB,goal)
    #print(x,y,goal)
    listX = [(goal[0]-bpB[0]*i)/bpA[0] for i in range(1,101)]
    listPossibility = []
    for i in range(len(listX)):
        if int(listX[i]) == listX[i]:
            listPossibility.append([int(listX[i]),i+1])
    minVal = math.inf
    for x,y in listPossibility:
        if (bpA[1]*x+bpB[1]*y == goal[1]):
            val = 3*x+y
            #print(x,y,val)
            minVal = min(val,minVal)
    #print(minVal)
    return (input.readline()=='\n',minVal)

rotate = True
sum = 0
while(rotate):
    rotate,val = _1game()
    if val != math.inf:
        sum += val
print(sum)
