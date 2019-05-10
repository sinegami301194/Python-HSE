inFile = open('input.txt')
myDict = {}
for line in inFile:
    words = line.strip().split()
    for word in words:
        myDict[word] = myDict.get(word, 0) + 1
print(sorted(myDict.items(), key=lambda x: (-x[1], x[0]))[0][0])
