# 136ms
import sys
import heapq as hq

heap = []

num = int(sys.stdin.readline())

for _ in range(num):
    x = int(sys.stdin.readline())
    if x != 0:
        hq.heappush(heap, (abs(x), x))
    elif len(heap) < 1:
        print(0)
    else:
        print(hq.heappop(heap)[1])
