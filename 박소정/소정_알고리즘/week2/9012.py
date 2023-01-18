import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    temp = []
    x = input()
    for j in x:
        if j == '(':
            temp.append(j)
        elif j == ')':
            if temp:
                temp.pop()
            else:
                print("NO")
                break
    else:
        if temp:
            print("NO")
        else:
            print("YES")
