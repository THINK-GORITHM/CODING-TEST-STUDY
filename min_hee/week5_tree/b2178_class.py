# 백준 2178 미로 탐색
# 길찾기 (1,1) -> (M,N) 최단거리(BFS)

import sys 
from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline() for _ in range(N)]

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M 

def bfs():   
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True 
    dq = deque()
    dq.append((0, 0, 1))
    while dq:
        y, x, d = dq.popleft()
        
        # 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
        if y == N-1 and x == M-1:
            return d 
        
        nd = d +1 
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                dq.append((ny, nx, nd))
          
print(bfs())