import numpy as np

filePath = 'Day01/listOfCal.txt'

with open(filePath) as f:
    mylist = f.read().splitlines()

    tempSum = 0
    elfCal = []
    
    for row in mylist:
        if row != '':
            tempSum += int(row)
        else:
            elfCal.append(tempSum)
            tempSum=0


elfCalArr = np.asarray(elfCal)
elfCalArr.sort()

maxCalElf = elfCalArr[-1]
maxCalElfTop3Sum = sum(elfCalArr[-3:])

print(f"Max calories: {maxCalElf}")
print(f"Sum cal of top 3 elfs: {maxCalElfTop3Sum}")