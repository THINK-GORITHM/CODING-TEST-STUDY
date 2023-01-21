# 문제풀이 흐름 정리
# 카드의 개수 N, 가깝게 맞춰야 할 합계값인 M을 입력받음
# N만큼의 숫자 카드를 입력받아 배열로 저장
# N개의 카드 중 3가지의 조합을 모두 살펴보며, 합계값을 M과 비교하는 완전 탐색 알고리즘 사용
# --> 시간 복잡도 = O(N^2) => N의 최댓값 : 100, 100^2 < 1억이므로 시간초과 안 남

from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = -1
diff = m
for c in combinations(cards, 3):
    if (sum(c) <= m) & (diff > (m-sum(c))):
        diff = m-sum(c)
        result = sum(c)
print(result)