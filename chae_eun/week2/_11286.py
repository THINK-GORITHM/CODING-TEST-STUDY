import heapq
import sys
# 자동으로 가장 작은 값이 맨 위로 저장
N = int(input())
pq = []
for _ in range(N):
    num = int(sys.stdin.readline());
    if num == 0: 
        if pq:
            print(heapq.heappop(pq)[1])
        else: print(0)
    else: 
        heapq.heappush(pq, (abs(num), num))
