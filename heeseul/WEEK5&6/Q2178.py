from collections import deque

dy = (0, 1, 0, -1)  #행 움직임의 상대좌표
dx = (1, 0, -1, 0)  #열 움직임의 상대좌표
N, M = map(int, input().split())
path = [input() for _ in range(N)]

def is_valid(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs():
    check = [[False] * M for _ in range(N)]
    check[0][0] = True  #처음 시작점을 True로 해놓고 시작
    dq = deque()
    dq.append((0, 0, 1))   #탐색할 것의 정보 넣어줌 (좌표, 거리)

    while dq:
        y, x, d = dq.popleft()

        if y == N - 1 and x == M - 1: #맨 마지막에 도착한 경우
            return d

        nd = d + 1

        for i in range(4):  # 다음으로 갈 수 있는 좌표 생성
            ny = y + dy[i]
            nx = x + dx[i]
            #유효한 좌표이고 갈 수 있는 좌표이고 방문하지 않았던 좌표라면
            if is_valid(ny, nx) and path[ny][nx] == '1' and not check[ny][nx]:
                check[ny][nx] = True    #방문했음을 표시
                dq.append((ny, nx, nd))     #큐에 좌표 정보 넣어줌

print(bfs())