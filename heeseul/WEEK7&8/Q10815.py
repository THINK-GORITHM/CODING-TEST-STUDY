#결과를 문자열로 저장하면 시간초과남
from bisect import bisect_left, bisect_right

N = int(input())    # N : 상근이가 가지고 있는 숫자 카드 개수
card = list(map(int, input().split()))  # card : 숫자 카드에 적혀있는 정수 리스트
card.sort()
M = int(input())    # M : 주어진 정수 개수
num = list(map(int, input().split()))   # num : 주어진 정수 리스트
result = "" #결과 문자열

for n in num:
    exist = bisect_right(card, n)-bisect_left(card, n)
    result += str(1 if exist == 1 else 0)+" "

print(result)