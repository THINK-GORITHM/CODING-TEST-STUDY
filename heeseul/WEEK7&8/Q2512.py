N = int(input())    # N : 지방의 수
require = list(map(int, input().split()))   # require : 각 지방의 예산 요청들
M = int(input())    # M : 총 예산

start = 0   #탐색 범위의 시작
end = max(require) #탐색 범위의 끝부분을 최고요청금액으로 초기화

if sum(require) <= M: #예산 요청 금액의 합이 총 예산보다 같거나 적을 경우
    print(end)
else:   #예산 요청 금액의 합이 총예산보다 많을 경우
    #이진 탐색 반복
    while start <= end:
        mid = (start + end) // 2    #상한액
        high = 0    #내가 책정한 총예산
        for r in require:
            if r <= mid: #상한액 >= 요청예산액
                high += r   #내가 책정한 총예산에 요청예산액을 더해줌
            else:   #상한액 < 요청예산액
                high += mid     #내가 책정한 총예산에 상한액을 더해줌

        if high > M:    #내가 책정한 총 예산이 총예산보다 큰 경우 => 상한액을 낮춰야 함
            end = mid - 1    #탐색범위의 끝부분을 상한액-1로 갱신해줌 => 기존 상한액보다 적은 범위에서 상한액을 책정할 수 있도록
        else:
            start = mid + 1   #탐색범위의 시작부분을 상한액+1로 갱신해줌 => 기존 상한액보다 큰 범위에서 상한액을 책정할 수 있도록
    print(end)