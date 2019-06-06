str = input() # Input the string
newStr = str[::-1]
posBegin = str.find('h', 0)
posEnd = len(str) - newStr.find('h', 0) - 1
answer = str[:posBegin] + str[posEnd + 1:]
print(answer, end='')
