N = int(input())
myDict = {}
for i in range(N):
    f_word, s_word = input().split()
    myDict[f_word] = s_word
    myDict[s_word] = f_word
print(myDict[input()])
