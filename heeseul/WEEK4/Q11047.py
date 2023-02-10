import sys
n, k = map(int, sys.stdin.readline().split())
val = [int(sys.stdin.readline()) for i in range(n)] #가치를 담을 리스트
val.reverse() #내림차순으로 변경
count = 0 #필요한 동전 개수
cal = k #남은 총합

for v in val:
    if v > cal: #남은 총합보다 가치단위가 더 크다면 다음 단위로 넘기기
        continue
    else:
        count += cal // v #필요한 동전 개수 구하기
        cal %= v #남은 총합 계산
        if cal == 0: #만약 총합을 다 채웠다면 나가기
            break
print(count)