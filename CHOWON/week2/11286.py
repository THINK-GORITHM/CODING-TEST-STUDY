# 문제풀이 흐름 정리
# 총 연산 횟수 N 입력받고, N만큼 크기의 배열 생성
# N만큼 돌면서 정수 x 입력받아 각 경우에 맞는 연산해주기
# (x != 0) -> x값 배열에 추가
# (x == 0) -> 배열의 절댓값의 최솟값 출력 및 삭제 (배열에 아무것도 없으면 0 출력)
# 단, 배열내의 같은 (절댓값의)최솟값이 여러 개이면 최솟값 출력 및 삭제(똑같은 모든 값 다 삭제하는거 아니고)
# 요소 추가 시, 최솟값을 자동으로 루트 노드에 저장하는 heapq (min-heap) 사용
# 절댓값의 대소 비교도 필요하므로, 입력 값 x 뿐만 아니라, x의 절댓값도 저장해서 비교해야 함

# 복잡도 예상
# 총 연산 횟수 N의 최댓값 : 100,000 -> N에 대한 2중 반복문은 시간초과
# heapq.heappush -> O(logT)
# heapq.heappop -> O(logN)

import sys
import heapq

h = []

for _ in range(int(input())):
    x = int(sys.stdin.readline())
    if x:
        # 배열 h에 x의 절댓값과 그냥 값(?) 두 개를 튜플로 저장
        # heapq에 튜플 형태로 값을 저장할 경우, 튜플의 첫 번째 요소를 기준으로 min-heap 구성
        # (max-heap을 구성하고 싶으면 튜플의 첫 번째 요소에 -1을 곱해준 값을 넣어주기)
        heapq.heappush(h, (abs(x),x)) 
    else:
        if len(h) == 0:
            print(0)
        else:
            # Python의 heapq는 min-heap이라 0번째 요소(루트노드)가 최솟값임
            print(h[0][1]) # 배열의 0번째 요소의 두번째 값 -> 그냥 x값
            heapq.heappop(h)