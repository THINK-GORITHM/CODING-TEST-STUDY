import sys
input = sys.stdin.readline
N, M = map(int, input().split()) #칭호 개수, 캐릭터 개수
power = []

for _ in range(N):
    power.append(input().split()) #칭호와 값을 묶어서 저장
    if len(power) > 1:
        if power[-1][1] == power[-2][1]: #칭호와 그 다음 칭호의 값이 같다면
            power.pop() #더 나중의 칭호를 제거

for _ in range(M):
    p = int(input()) #전투력 입력받기
    start, end = 0, len(power)-1
    while start <= end:
        mid = (start + end) // 2
        if p <= int(power[mid][1]):
            end = mid - 1
        else:
            start = mid + 1
    print(power[end+1][0])




