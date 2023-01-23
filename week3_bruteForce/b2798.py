# 백준 2798 블랙잭
# 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대로
# N:카드의 개수, M: 맍들고자하는 수
from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0 

for i in combinations(cards, 3):
    i_sum = sum(i)
    if result < i_sum <= M:
        result = i_sum
print(result)