# 백준 11047 동전 0
# N: 동전의 총 종류 K: 합
# 4200 = 1000*4 

import sys

N, K = map(int, sys.stdin.readline().split())
coins = []

for _ in range(N):
    coins.append(int(sys.stdin.readline().strip()))

cnt = 0
for i in reversed(coins):
    cnt += int(K/i)
    K %= i
        
print(cnt)
