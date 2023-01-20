# 80ms
from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
num = 0

for i in combinations(card, 3):
    temp = sum(i)
    if num < temp <= m:
        num = temp

print(num)
