str = input()
posBegin = str.find('f', 0)
if str.find('f', posBegin + 1) != -1:
    newStr = str[::-1]
    posEnd = len(str) - newStr.find('f', 0) - 1
    print(posBegin, posEnd, end='')
if str.find('f', posBegin + 1) == -1 and posBegin != -1:
    print(posBegin, end='')
