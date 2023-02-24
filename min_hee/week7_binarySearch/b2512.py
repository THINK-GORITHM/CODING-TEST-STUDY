# 백준 2512 예산 ==> 이분탐색으로 푸는 문제인데.. 그냥 구현으로 풀어보니깐 틀림
# 예산 배정 원칙 
# 1. 모든 요청이 배정될 수 있는 경우 - 요청한 금액 그대로 배정
# 2. 없는 경우 - 특정한 정수 상한액을 계산하여 이상이면 상한액 배정, 이하면 그대로

# N: 지방의 수
# 지방별 예산 요청 budgets 
# 총 예산 total
# -> 배정된 예산중 최댓값인 정수 출력 ans 

# 110 120 140 150 (total: 485)
# 1. 4개를 더했을때, 520 (x)
# 2. 3개를 더했을때, 115가 상한선 (x)
# 3. 2개를 더했을때, 127이 상한선 (o) 가능 

import sys 
from bisect import bisect_left, bisect_right

N = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
total = int(sys.stdin.readline())

ans = 0 
# 경우 1. 모든 요청이 배정될 수 있는 경우 
if sum(budgets) <= total:
    ans = max(budgets)
    
# 경우 2. 모든 요청이 배정될 수 없는 경우 (상한가 출력)
else: 
    budgets.sort()
    sum_budgets = 0
    ans = 0
    
    for i in range(N):
        sum_budgets += budgets[i]

        if N-i-1 == 0 and (budgets[i] > total-sum_budgets):
            sum_budgets -= budgets[i]
            break
        
        elif (budgets[i] > (total - sum_budgets)/(N-i-1)):
            sum_budgets -= budgets[i]
            break
        
        ans = (total-sum_budgets)/(N-i-1)
        
    # i=0: sum: 110 < total-sum/3 = 125
    # i=1: sum: 230 120 < total-sum/2 = 127.5 
    # i=2: sum: 370 140 > total-sum/1 = 115 => break => 1로 되돌아감
    
print(int(ans))