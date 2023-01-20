# 140ms
import sys

n = int(sys.stdin.readline())
r = 0

for _ in range(n):
    s = []
    word = sys.stdin.readline().rstrip()

    s.append(word[0])

    for i in range(1, len(word)):
        if len(s) == 0:
            s.append(word[i])
        else:
            top = s[-1]

            if word[i] == top:
                s.pop()
            else:
                s.append(word[i])

    if len(s) == 0:
        r += 1

print(r)
