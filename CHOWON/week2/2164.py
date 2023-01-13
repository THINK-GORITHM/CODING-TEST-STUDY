# 문제풀이 흐름 정리
# step0) N 입력받고, 오름차순으로 정수 배열 생성 (가장 작은 수부터 왼쪽에 있다고 가정)
# step1) 가장 작은 수 버리기 (popleft)
# step2) 버리고 남은 수 중에 가장 작은 수를 맨 위(배열 상, 맨 오른쪽)로 옮기기 (append)
# step3) 배열에 남은 정수가 1개일 때까지 step1,2를 반복 실행
# 왼쪽에서 빼고, 오른쪽으로 다시 붙여 넣는 과정을 위해서는 양 쪽이 다 뚫린(?) Queue 사용

# 복잡도 예상
# N 입력 최댓값 -> 500,000
# 단순 반복문은 괜찮지만 2중부터는 바로 시간초과

from collections import deque

q = deque()
n = int(input())
for i in range(1, n+1):
    q.append(i)   # append 시간 복잡도 : 1

while len(q) > 1:
    q.popleft()   # popleft 시간 복잡도 : 1
    q.append(q.popleft())

print(q.pop())   # pop 시간 복잡도 : 1