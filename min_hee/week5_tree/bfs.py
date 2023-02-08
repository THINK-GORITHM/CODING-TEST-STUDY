# BFS 구현 
from collections import deque

adj = [[0] * 13 for _ in range(13)] # 13 * 13 짜리 행렬 
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1 
# ... 들어가는 간선을 정의 

# 재귀함수
def bfs():
    dq = deque()
    dq.append(0) # root 노드
    while dq: 
        now = dq.popleft()
        print(now)
        for nxt in range(13):
            if adj[now][nxt] == 1:
                dq.append(nxt)
                
bfs()