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
    goal[0] += 10000000000000
    goal[1] += 10000000000000
    
    #print(bpA,bpB,goal)
    
    # a*x1 + b*x2 = x
    # a*y1 + b*y2 = y
    
    # a = (x-x2*b)/x1
    # b = (y*x1-y1*x)/(x1*y2 - y1*x2)
    
    b = (goal[1]*bpA[0]-bpA[1]*goal[0])//(bpA[0]*bpB[1]-bpA[1]*bpB[0])
    a = (goal[0]-bpB[0]*b)//bpA[0]
    
    if b > 0 and a > 0 and bpA[0]*a+bpB[0]*b == goal[0] and bpA[1]*a+bpB[1]*b == goal[1]:
        return (input.readline()=='\n',a*3+b)
    return (input.readline()=='\n',0)

rotate = True
sum = 0
while(rotate):
    rotate,val = _1game()
    print(val)
    sum += val
print(sum)