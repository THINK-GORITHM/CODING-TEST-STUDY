# 문제풀이 흐름 정리
# 정수를 저장하는 스택 구현해보는 문제
# push / pop / size / empty / top 의 총 5가지 기능 구현 요구
# 배열을 통해 스택 구현

# push -> append 메소드 사용 (시간 복잡도 : 1)
# pop -> pop 메소드 사용 (시간 복잡도 : 1) 
# size -> len 메소드 사용 (시간 복잡도 : 1)
# empty -> len 메소드 사용 (시간 복잡도 : 1)
# top -> 스택의 가장 위, 즉, 배열에 가장 마지막에 추가된 요소에 접근 (시간 복잡도 : 1)

# 복잡도 예상
# 위 모든 기능에 대해 시간 복잡도가 1이므로, 총 소요되는 시간은 명령어의 개수만큼이라고 봐도 될 듯
# 입력되는 명령의 개수 -> 최대 10,000개
# 시간 제한이 0.5초이므로, 최대 입력 명령에 대해 2중 반복문부터는 시간초과

import sys

def stackFunc(s, inputs):
	if inputs[0] == "push":
		s.append(int(inputs[1]))
	elif inputs[0] == "pop":
		if len(s) > 0:
			print(s.pop())
		else:
			print(-1)
	elif inputs[0] == "size":
		print(len(s))
	elif inputs[0] == "empty":
		if len(s) == 0:
			print(1)
		else:
			print(0)
	elif inputs[0] == "top":
		if len(s) == 0:
			print(-1)
		else:
			print(s[-1])

input = sys.stdin.readline   # 빠른 입력을 위한 함수(이거 안 쓰면 시간초과,,)
n = int(input())
s = []

for i in range(n):
  # 입렵값 inputs를 '명령어'와 '정수'로 쪼개서(split) 함수에 전달
	inputs = input().split()
	stackFunc(s, inputs)