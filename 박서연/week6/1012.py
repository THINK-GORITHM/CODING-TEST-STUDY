# 96ms
import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False  # 공간 넘어가면 끝냄
    if matrix[x][y] == 1:
        matrix[x][y] = 0  # 확인완료

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True

    return False


T = int(input())

for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    matrix = [[0] * N for _ in range(M)]

    # 배추심기
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    for x in range(M):
        for y in range(N):
            if dfs(x, y) == True:
                cnt += 1

    print(cnt)
