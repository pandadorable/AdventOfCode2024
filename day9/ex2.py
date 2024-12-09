input = list(map(int,open("./day9/input.txt").readline().strip('\n')))
disk = []
id = 0
isFile = True
for x in input:
    sub = []
    for _ in range(x):
        if isFile:
            sub.append(id)
        else:
            sub.append('.')
    if len(sub) > 0:
        disk.append(sub)
    if isFile:
        id += 1
    isFile = not isFile
#print(disk)

id = len(disk)-1
while(id >=0):
    #print(id,disk[id])
    if '.' not in disk[id]:
        for i in range(id):
            if '.' in disk[i] and len(disk[i]) >= len(disk[id]):
                for _ in range(len(disk[id])):
                    #print("reduce ", end='')
                    disk[i].pop()
                if len(disk[i]) == 0:
                    #print('remove ',end='')
                    disk.pop(i)
                    id -= 1
                box = disk[id]
                disk[id] = ['.' for _ in range(len(disk[id]))]
                #print(box)
                disk.insert(i,box)
                id += 1
                break
    id -= 1
    
sum = 0
list = []
for box in disk:
    for v in box:
        list.append(v)
for i in range(len(list)):
    if list[i] != '.':
        sum += i*list[i]
print(sum)