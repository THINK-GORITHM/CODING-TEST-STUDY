# 문제풀이 흐름 정리
# 소괄호 한 쌍이 온전히 있으면 VPS라고 함
# 입력값으로 들어오는 소괄호 덩어리(?)가 VPS인지 아닌지 출력

# 한 줄에 들어오는 소괄호 덩어리를 쪼개서 배열에 저장해두고, 
# 배열을 돌면서 VPS가 만들어지는지 봐야함
# VPS 만들어지면 그냥 없애버리고, 
# 배열 탐색의 맨 마지막에 짝 못 찾고 남은 소괄호가 있는지 여부로 YSE/NO 결정 

# 복잡도 예상
# 소괄호 덩어리 개수 T의 최댓값 -> ??뭐임 왜 문제에 없어
# 각 소괄호 덩어리의 길이 최댓값 -> 50
# T만큼 반복문 한 번 돌면서 * 그 안에서 소괄호 덩어리의 길이만큼 반복문을 또 도는 2중 반복문
# T * 60이 시간 복잡도인데,,,아니 왜 문제에 T 최댓값없음; 암튼 O(T)니까 T <= 1억이면 될 듯

for i in range(int(input())):
    vpsList = list(input())  # 한 줄의 입력으로 들어오는 소괄호 덩어리가 소괄호마다 쪼개져 저장된 리스트
    result = []
    for p in range(0,len(vpsList)):
        # VPS가 되려면 무조건 '('는 있어야 함
        # '('가 나오면 무조건 append하고, 
        # ')'가 나오면 result에 쌓인 짝 못 찾은 '('가 있으면 둘이 대충 VPS 됏다치고 result.pop()
        if vpsList[p] == '(':
            result.append('(')
        elif vpsList[p] == ')':
            if len(result) == 0:
                result.append(')')
                break
            else:
                result.pop()
    
    if len(result) == 0:
        print("YES")
    else:
        print("NO")