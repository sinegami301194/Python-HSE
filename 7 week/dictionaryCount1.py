strWords = '' # Creating string
counter = {} # Creating empty dictionary
f = open('input.txt', 'r') # Open file for reading
for line in f: # Start the cycle
    strWords = strWords + ' ' + line.replace('\n', '')
f.close()
for word in strWords.split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
