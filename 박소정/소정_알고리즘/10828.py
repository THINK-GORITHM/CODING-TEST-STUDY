import sys

input = sys.stdin.readline

T = int(input())
stack = []

for _ in range(T):
    command = input().split()
    if command[0] == "push":
        stack.append(int(command[1]))
    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1]) # 음수 = 맨 뒤
