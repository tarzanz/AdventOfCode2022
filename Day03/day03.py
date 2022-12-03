
filePath = 'Day03/inventoryContent.txt'

# Wrong: 9830

with open(filePath) as f:
    mylist = f.read().splitlines()
    sum = 0

    for row in mylist:
        
        str1 = row[:int(len(row)/2)]
        str2 = row[int(len(row)/2):]

        for mychar in str1:
            numOfChar = str2.count(mychar)
            if numOfChar > 0:
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
                sum += val + valOffset
                break

print(f"Sum of item: {sum}")