def stack(n):
    stack = []
    for i in n:
        if(i == '('): stack.append('(')
        elif len(stack) == 0: return "NO"
        else: stack.pop()
    
    if len(stack) == 0: return "YES"
    else: return "NO"

n = int(input())

for _ in range(n):
    answer = input()
    print(stack(list(answer)))
    