strWords = ''
counter = {}
f = open('input.txt', 'r')
for line in f:
    strWords = strWords + ' ' + line.replace('\n', '')
f.close()
for word in strWords.split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
