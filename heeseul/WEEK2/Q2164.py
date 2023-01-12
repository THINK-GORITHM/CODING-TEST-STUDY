from collections import deque
import sys

card = int(sys.stdin.readline())
dq = deque()

for i in range(card):
    dq.appendleft(i+1)

while len(dq) > 1:
    dq.pop()
    dq.rotate(1)

print(dq.pop())
