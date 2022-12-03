
filePath = 'Day03/inventoryContent.txt'

def calcPrio(mychar):
    val = ord(mychar)
    # Check if char in lower case or upper case.
    # If ASCII code is larger than 96, its lower.
    if val > 96:
        # 'a' shall result in 1, hence the offset is -96
        # from ASCII code valie
        valOffset = -96
    else:
        # For upper case, the offsert is smaller
        valOffset = -64+26
    return val + valOffset

with open(filePath) as f:
    mylist = f.read().splitlines()
    sum = 0

    for row in mylist:
        
        str1 = row[:int(len(row)/2)]
        str2 = row[int(len(row)/2):]

        for myChar in str1:
            numOfChar = str2.count(myChar)
            if numOfChar > 0:
                prio = calcPrio(myChar)
                sum += prio
                break

print(f"Sum of item (part 1): {sum}")

with open(filePath) as f:
    mylist = f.read().splitlines()
    sum2 = 0

    numLines = len(mylist)
    i = 0
    while i<numLines:
        s1 = set(mylist[i])
        i += 1
        s2 = set(mylist[i])
        i += 1
        s3 = set(mylist[i])
        i += 1

        myChar = s1.intersection(s2).intersection(s3).pop()
        sum2 += calcPrio(myChar)
        
print(f"Sum of item (part 2): {sum2}")
# Wrong: 1300