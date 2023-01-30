import sys
N, L = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
s.sort() #새는 위치 오름차순 정렬
cnt = 1 #테이프 개수

start = s[0] #테이프 시작 지점
for location in s[1:]: #물이 새는 위치 할당
    if location in range(start, start+L): #테이프 범위 내에 물이 새는 곳이 있다면
        continue #원래 테이프 사용
    else: # 테이프 범위 내에 물이 새는 곳이 없다면
        start = location #테이프 범위 시작점 바꿔주고
        cnt += 1 #테이프 개수 늘려줌
print(cnt)
