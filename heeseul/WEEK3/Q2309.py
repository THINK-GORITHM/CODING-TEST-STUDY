from itertools import combinations
import sys

h = []
for _ in range(0, 9):
    h.append(int(sys.stdin.readline()))
for i in combinations(h, 7):
    sum(i)
    if sum(i) == 100:
        c = sorted(i)
        break
for a in range(7):
    print(c[a])
