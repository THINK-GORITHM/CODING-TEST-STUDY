# 문제풀이 흐름 정리
# 9개의 키를 입력받아서 배열에 저장하기
# 키 배열에서 무작위로 7개를 뽑아 총 합의 값을 구하여 100인 경우가 정답
# 합 연산에 순서는 상관는 없으므로, 조합(Combination) 연산을 사용

# 입력이 무조건 9개 뿐이므로, 시간 복잡도는 조합 연산에 따른 9^2가 됨

from itertools import combinations

heights = []

for _ in range(9):
    heights.append(int(input()))

result = []
for combi in combinations(heights, 7):
    if sum(combi) == 100:
        result = combi

result = sorted(result)
for i in range(7):
    print(result[i])