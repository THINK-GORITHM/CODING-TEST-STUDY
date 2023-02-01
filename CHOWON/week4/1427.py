# 문제풀이 흐름 정리
# (영선아 나무를 왜 베어가)
# n = 나무의 개수이자 영선이가 나무를 베러갈 날짜 수
# 원래 나무의 길이 배열, 나무의 성장 속도 배열 입력받기
# 나무의 초깃값(길이)과 성장속도를 2차원 배열에 추가 및 정렬을 통해 가장 빨리 많이 자라는 나무를 선택

n = int(input())                       
Hi = list(map(int, input().split()))    
Ai = list(map(int,input().split()))  

arr = []
total = 0

for i in range(n):                  
    arr.append([Hi[i], Ai[i]])

arr.sort(key = lambda x:x[1])       

for i in range(n):
    total += arr[i][0] + arr[i][1] * i

print(total)