from itertools import combinations
card, total = map(int, input().split())
num = list(map(int, input().split()))
m = 0
for i in combinations(num, 3):
    if sum(i) <= total:
        if m < sum(i):
            m = sum(i)
print(m) 