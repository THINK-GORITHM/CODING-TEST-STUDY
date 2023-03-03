# 65ms
import sys

input = sys.stdin.readline

n = int(input())
req = list(map(int, input().split()))
total = int(input())
start, end = 0, max(req)

while start <= end:
    mid = (start + end)//2
    bgt = 0
    for i in req:
        if i >= mid:
            bgt += mid
        else:
            bgt += i
    if bgt <= total:
        start = mid + 1
    else:
        end = mid - 1

print(end)
