import sys

N, M = map(int, input().split())

data = list(map(int, sys.stdin.readline().split()))

maxNum = 0;

for i in range(N-2):
    for j in range(i+1, N-1):
        for z in range(j+1, N):
            sumNum = data[i] + data[j] + data[z]
            if sumNum<= M : maxNum = max(maxNum, sumNum)

print(maxNum)

