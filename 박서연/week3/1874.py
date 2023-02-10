# 188ms
import sys

n = int(sys.stdin.readline())
s = []
r = []
now = 1
temp = 0
for _ in range(n):
    num = int(sys.stdin.readline())
    while now <= num:
        s.append(now)
        r.append("+")
        now += 1
    if s[-1] == num:
        s.pop()
        r.append("-")
    else:
        print("NO")
        temp = 1
        break

if temp == 0:
    for i in r:
        print(i)
