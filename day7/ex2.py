input = open("./day7/input.txt")
sum = 0
for l in input.readlines():
    result,values = l.split(':')
    result = int(result)
    values = list(map(int,values.split()))
    #print(result,values)
    combination = [values[0]]
    for x in range(1,len(values)):
        nextList = [values[x]+v for v in combination]+[values[x]*v for v in combination]+[int(str(v)+str(values[x])) for v in combination]
        combination = nextList
        #print(combination)
    if result in combination:
        sum += result
print(sum)