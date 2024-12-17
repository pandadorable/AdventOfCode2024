import re
input = open("./day17/input.txt")
A = list(map(int, re.findall(r'\d+', input.readline())))[-1]
B = list(map(int, re.findall(r'\d+', input.readline())))[-1]
C = list(map(int, re.findall(r'\d+', input.readline())))[-1]
input.readline()
PROGRAM = list(map(int, re.findall(r'\d+', input.readline())))
POINTER = 0
OUTPUT = []
print(A,B,C)
print(PROGRAM)

def getCombo(operand):
    global A, B, C
    match(operand):
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case _:
            return 0
        
def adv(operand):
    print("adv",operand)
    global A
    A = int(A/(2**getCombo(operand)))

def bxl(operand):
    print("bxl",operand)
    global B
    B = B ^ operand
    
def bst(operand):
    print("bst",operand)
    global B
    B = getCombo(operand)%8
    
def jnz(operand):
    print("jnz",operand)
    global POINTER, A
    if A != 0:
        POINTER = operand-2
        
def bxc(operand):
    print("bxc",operand)
    global B, C
    B = B ^ C
    
def out(operand):
    print("out",operand)
    global OUTPUT
    OUTPUT.append(getCombo(operand)%8)

def bdv(operand):
    print("bdv",operand)
    global A, B
    B = int(A/(2**getCombo(operand)))

def cdv(operand):
    print("cdv",operand)
    global A, C
    C = int(A/(2**getCombo(operand)))

def runCommand(command,operand):
    match(command):
        case 0:
            adv(operand)
        case 1:
            bxl(operand)
        case 2:
            bst(operand)
        case 3:
            jnz(operand)
        case 4:
            bxc(operand)
        case 5:
            out(operand)
        case 6:
            bdv(operand)
        case 7:
            cdv(operand)
    global POINTER
    POINTER += 2
            
while(POINTER < len(PROGRAM)):
    runCommand(PROGRAM[POINTER],PROGRAM[POINTER+1])
    print(A,B,C)
    print('OUTPUT : ',end='')
    for c in OUTPUT:
        print(str(c)+',',end='')
    print()