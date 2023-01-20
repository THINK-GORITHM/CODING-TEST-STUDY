import sys
n = int(sys.stdin.readline())
stack = []
result = []
isValid = True
p = 1 #push할 수

for i in range(0, n):
    num = int(sys.stdin.readline())
    while p <= num: #입력받은 배열 원소만큼 스택 채우기
        stack.append(p)
        result.append('+')
        p += 1
    if stack[-1] != num: #스택의 마지막 원소와 입력 받은 배열원소의 수가 다르다는 것은
                         #배열 원소보다 큰 값이 스택에 있다는 뜻이므로 꺼낼 수 없다. 따라서 불가능한 경우
        isValid = False
        break
    else:
        stack.pop()
        result.append('-')

if not isValid:
    print("NO")
else:
    [print(i) for i in result]
