
filePath = 'Day05/moveOrders.txt'

with open(filePath) as f:
    mylist = f.read().splitlines()

    startStackRow = 8
    numStacks = 9

    stacks = [[] for _ in range(numStacks)]

    # Generate stacks from file
    for row in reversed(mylist[:startStackRow]):
        stackRow = row[1::4]
        for i, stack in enumerate(stacks):
            if not stackRow[i] == ' ':
                stack.append(stackRow[i])

    for row in mylist[startStackRow+2:]:
        containersToMove = int(row[row.find('move')+5:row.find('from')-1])
        idxFrom = int(row[row.find('from')+5:row.find(' to')])
        idxTo = int(row[-1])

        for i in range(containersToMove):
            container = stacks[idxFrom-1].pop()
            stacks[idxTo-1].append(container)
    
    result = ''
    for stack in stacks:
        result += stack[-1]
    print(f"Result part 1: {result}")
