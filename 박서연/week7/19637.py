# 400 ms
import sys

input = sys.stdin.readline


def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if target > power[mid]:
            start = mid + 1
        else:
            end = mid - 1
    print(name[end + 1])


N, M = map(int, input().split())
name = []
power = []

for _ in range(N):
    a, b = input().split()
    name.append(a)
    power.append(int(b))

for _ in range(M):
    binary_search(int(input()), 0, N-1)
