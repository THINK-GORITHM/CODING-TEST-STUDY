#블로그 참고
#인접한 배추들을 한 묶음으로 만든다
#배추의 묶음만큼 지렁이를 추가한다
#2차원 리스트를 이용하여 배추밭을 표현할 그래프를 만들고 배추가 있는 자리에는 1을, 없는 자리에는 0을 부여
#dfs 함수가 배추밭 그래프를 탐색하다가 배추를 발견하면, 그 배추와 인접하다고
#할 수 있는 배추들을 모두 0으로 표시해줌

#재귀함수 최대 깊이 설정
import sys
sys.setrecursionlimit(10**5)

def dfs(x, y):
    if (x<0 or x>N-1) or (y<0 or y>M-1):
        return False
    else:
        if graph[x][y] == 1:
            graph[x][y] = 0

            # 인접 좌표 생성 후 조사
            dfs(x, y+1)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x-1, y)
            return True
        return False

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split()) #열, 행, 심어져 있는 배추 개수
    graph = [[0] * M for _ in range(N)] #배추밭 그래프
    cnt = 0 #배추묶음 = 지렁이 수

    #배추 그래프 채우기
    for _ in range(K): #심어져 있는 배추 채우기
        y, x = map(int, input().split())
        graph[x][y] = 1

    for i in range(N):  #행
        for j in range(M):  #열
            if dfs(i, j):
                cnt += 1

    print(cnt)