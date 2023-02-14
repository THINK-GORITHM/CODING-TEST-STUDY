import sys
from collections import deque


def BFS(index):
    q = deque()
    q.append(index)
    visited[index] = 1
    print(index, end=" ")
    while q:
        x = q.popleft()
        if visited[x] == 0:
            visited[x] = 1
            print(x, end=" ")
        for i in range(1, vertex + 1):
            if graph[x][i] != 0 and visited[graph[x][i]] == 0:
                q.append(graph[x][i])


def DFS(index):
    if visited[index] == 0:
        visited[index] = 1
        print(index, end=" ")  # 실제 어떤 인덱스의 값이 선택 되었는지?
        for i in range(1, vertex + 1):
            if graph[index][i] != 0 and visited[graph[index][i]] == 0:
                DFS(graph[index][i])


vertex, edge, num = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(vertex + 1)]
graph = [[0] * (vertex + 1) for _ in range(vertex + 1)]  # 인접 행렬

for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = b
    graph[b][a] = a

DFS(num)
print()
visited = [0 for _ in range(vertex + 1)]
BFS(num)
