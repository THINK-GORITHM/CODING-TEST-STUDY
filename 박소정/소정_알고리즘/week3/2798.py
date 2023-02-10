import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
total = 0
for i in range(N):
    for j in range(i+1, N):
        for z in range(j+1, N):
            temp = cards[i]+cards[j]+cards[z]
            if temp <= M:
                total = max(total, temp)

print(total)

