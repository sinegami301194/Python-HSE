import random


A = list(map(int, input().split()))
B = list(map(int, input().split()))


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


def merge(A, B):
    C = A + B
    return C
C = merge(A, B)
B = quicksort(C)
print(*B, end='')
