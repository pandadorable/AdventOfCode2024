input = list(map(int,open("./day9/input.txt").readline().strip('\n')))
disk = []
id = 0
isFile = True
for x in input:
    for _ in range(x):
        if isFile:
            disk.append(id)
        else:
            disk.append('.')
    if isFile:
        id += 1
    isFile = not isFile
print(disk)
while(True):
    try :
        posDot = disk.index('.')
        val = disk.pop()
        if val != '.':
            disk[posDot] = val
    except ValueError :
        break
print(disk)
sum = 0
for index in range(len(disk)):
    sum += index*disk[index]

print(sum)