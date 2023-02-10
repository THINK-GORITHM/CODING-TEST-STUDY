T = int(input())

for p in range(T):
    s = []
    isVPS = True
    for a in input():
        if a == '(':
            s.append(a)
        else:
            if len(s) > 0:
                s.pop()
            else:
                isVPS = False
                break
    if len(s) > 0:
        isVPS = False;

    if isVPS:
        print("YES")
    else:
        print("NO")
