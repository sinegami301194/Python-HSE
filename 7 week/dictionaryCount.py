inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')


myDict = {}
myList = []
lines = inFile.readlines()
for line in lines:
    for i in line.split(' '):
        myList.append(i)
for elem in myList:
    myDict[elem] = myDict.get(elem, 0) + 1
    print(myDict[elem] - 1, end=' ', file=outFile)
inFile.close()
inFile.close()
