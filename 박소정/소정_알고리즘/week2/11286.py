import sys, heapq as hq
input = sys.stdin.readline
N = int(input())
min = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if len(min) == 0:
            print(0)
        else:
            print(hq.heappop(min)[1])
    else:
        hq.heappush(min, ((abs(x)), x))
