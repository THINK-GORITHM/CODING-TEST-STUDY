import heapq as hq
import sys

input = sys.stdin.readline
pq = []

for _ in range(int(input())):
    x = int(input())
    if x: #x가 0이 아닐 때
        hq.heappush(pq, (abs(x), x))
    else: #x가 0일 때
        print(hq.heappop(pq)[1] if pq else 0)
