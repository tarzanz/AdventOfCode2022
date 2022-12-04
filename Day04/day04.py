
filePath = 'Day04/listOfSections.txt'

def StrToNums(myStr):
    numList = myStr.split('-')
    return int(numList[0]), int(numList[1])

def OneContainTheOther(str1,str2):
    n1Low, n1High = StrToNums(str1)
    n2Low, n2High = StrToNums(str2)
    
    if n1Low <= n2Low and n1High >= n2High:
    # If n1 contains n2
        return True

    elif n2Low <= n1Low and n2High >= n1High:
    # If n2 contains n1
        return True
    
    else:
    # One does not completely overlap the other
        return False

def Overlapping(str1,str2):
    n1Low, n1High = StrToNums(str1)
    n2Low, n2High = StrToNums(str2)

    if n2Low <= n1Low and n2High >= n1Low:
        return True
    elif n1Low <= n2Low and n1High >= n2Low:
        return True
    else:
        # The segments does not overlap at all
        return False


with open(filePath) as f:
    mylist = f.read().splitlines()
    counterPart1 = 0
    counterPart2 = 0

    for row in mylist:
        splitLine = row.split(',')
        if OneContainTheOther(splitLine[0],splitLine[1]):
            counterPart1 += 1
        if Overlapping(splitLine[0],splitLine[1]):
            counterPart2 += 1

print(f"Number of completely overlaping assignments (part 1): {counterPart1}")
print(f"Number of partly overlaping assignments (part 2): {counterPart2}")