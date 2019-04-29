el1 = el2 = 0
a = int(input())
while a != 0:
    if a >= el1:
        el2 = el1
        el1 = a
    if el2 < a and a < el1:
        el2 = a
    a = int(input())
print(el2, end='')
