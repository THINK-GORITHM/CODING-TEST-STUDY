
import sys
from collections import deque 
n=int(sys.stdin.readline())
q=deque()

for i in range(1,n+1):
  q.appendleft(i)

while len(q)!=1:
  q.pop()
  q.appendleft(q.pop())

print(q.pop())




