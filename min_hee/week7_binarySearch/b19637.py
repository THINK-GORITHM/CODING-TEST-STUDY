# 백준 19637 
# 이분탐색 
# characters: WEAK, .. , A 
# powers: 10000, 100000

import sys 
from bisect import bisect_left

N, M = map(int, sys.stdin.readline().split())

characters = []
powers = []

for _ in range(N):
    character, power = sys.stdin.readline().split()
    characters.append(character)
    powers.append(int(power))
    
# characters = [WEAK, NORMAL, STRONG]
# powers = 10000, 100000, 1000000
    
arr = [int(sys.stdin.readline()) for _ in range(M)]
for i in arr:
    # 9999 -> 0
    # 10001 -> 1
    print(characters[bisect_left(powers, i)])