# DFS 구현 
# 인접행렬(or 인접리스트) adj
adj = [[0] * 13 for _ in range(13)] # 13 * 13 짜리 행렬 
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1 
# ... 들어가는 간선을 정의 

# 재귀함수
def dfs(now): # now: 현재 방문한 노드
    for nxt in range(13): # nxt: 다음 방문하려는 노드
        if adj[now][nxt] == 1:
            print(nxt)
            dfs(nxt)
            
dfs(0) # 루트노드 0으로 시작