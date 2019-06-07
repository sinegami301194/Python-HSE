myList = input() # Input the list
a = myList.split()
for i in range(0, len(a)):
    if i % 2 == 0:
        print(a[i], end=' ')
