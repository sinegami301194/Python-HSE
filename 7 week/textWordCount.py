inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')


text = []
A = []
mySet = set()
lines = inFile.readlines()
for line in lines:
    text.append(list(line.split()))
for i in range(0, len(text)):
    A += text[i]
mySet = set(A)
print(len(mySet), file=outFile)
inFile.close()
outFile.close()
