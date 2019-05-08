N = int(input())
per = ''
sc = 0
myList = []
for i in range(N):
    (per, sc) = (tuple(input().split()))
    myList.append((per, int(sc)))
A = sorted(myList, key=lambda x: -x[1])
for i in A:
    print(i[0])
