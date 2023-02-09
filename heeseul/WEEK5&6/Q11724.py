# 간선의 개수가 많으므로 인접행렬 이용
import sys

sys.setrecursionlimit(10 ** 6)  # 재귀 횟수 늘려주기
input = sys.stdin.readline

N, E = map(int, input().split())  # N:정점 E:간선
adj = [[0] * N for _ in range(N)]  # 인접행렬 생성 및 초기화
check = [False] * N  # 방문여부를 확인할 배열
component = 0  # 연결요소 개수

# 인접행렬 채우기
for i in range(E):
    u, v = map(int, input().split())
    adj[u - 1][v - 1] = adj[v - 1][u - 1] = 1  # 인덱스니까 숫자-1 해줘야 함


def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not check[nxt]:  # adj 값이 1이고 방문한 적이 없다면
            check[nxt] = True  # 방문했음으로 표시하고
            dfs(nxt)


for i in range(N):
    if not check[i]:  # 방문하지 않았다면
        component += 1
        check[i] = True
        dfs(i)

print(component)
