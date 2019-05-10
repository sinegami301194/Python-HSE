import sys

myList = (str(sys.stdin.read()).split())
myLets = {}
for word in myList:
    myLets[word] = myLets.get(word, 0) + 1
myLets = [(fr, lt) for lt, fr in myLets.items()]


def makeSort(lws):
    return (-lws[0], lws[1])


myLets.sort(key=makeSort)
for i in range(len(myLets)):
    print(myLets[i][1])
