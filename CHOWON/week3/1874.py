# 문제는 어느정도 알겠지만 구현할 수 없는,,아래 주석처리 안 한 코드는 구글링을 통해 본 코드 참고 하였습니당
# 4주차에 또 들여다보겠숨미당,,,ㅜㅅㅜ

### 구현하려고 용쓴 흔적,, 
# n = int(input())
# stack = []  
# result = []
# opertors = []  # +,- 연산자를 담을 배열
# temp = []

# for i in range(n):
#     n = int(input())
#     temp.append(n)
#     opertors.append('+')
#     for p in range(n+1):
#         stack.append(p)
#     result.append(stack.pop())
#     opertors.append('-')


# # print(result)

# res = True
# for i in range(n):
#     print("result -> ", result)
#     print("stack -> ", stack)
#     if result[i] != temp[i]:
#         res = False

# if res:
#     print(opertors)
# else:
#     print("NO")


n = int(input())
stack = []
answer = []
flag = 0
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:       # 입력한 수를 만날 때 까지 오름차순으로 push
        stack.append(cur)
        answer.append("+")
        cur += 1
    # 입력한 수를 만나면 while문 탈출. 즉 cur = num일 때 까지 while문을 돌아 스택을 쌓는다.

    if stack[-1] == num:    # stack의 TOP이 입력한 숫자와 같다면
        stack.pop()         # 스택의 TOP을 꺼내 수열을 만들어 준다.
        answer.append("-")
    else:                   # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
        print("NO")         # 12345 처럼 오름차순으로 스택이 입력되는데
        flag = 1            # TOP이 num보다 크면 num은 TOP보다 더 아래에 쌓여있기 때문이다.
        break               

if flag == 0:
    for i in answer:
        print(i)