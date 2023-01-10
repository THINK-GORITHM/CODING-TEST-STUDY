# 배열 
arr = [10, 11, 12, 13]
arr[2] = 5 # [10, 11, 5, 13]

# 백터 
v = []
v.append((123, 456))
v.append((789, 987))
print("stack size:",len(v))
for p in v:
    print(p)
    
# 큐
from collections import deque
q = deque()
q.append(123)
q.append(456)
q.append(789)
print("queue size:",len(q)) # 3
while (len(q) > 0):
    print(q.popleft()) # 123 456 789
    
# 우선순위 큐 (힙)
import heapq
pq = []
heapq.heappush(pq, 456)
heapq.heappush(pq, 123)
heapq.heappush(pq, 789)
print("heap size:",len(pq)) # 3
while len(pq) > 0:
    print(heapq.heappop(pq))
    
# 맵 (딕셔너리)
m = {}
m["Yoondy"] = 40
m["Sky"] = 100
m["Jerry"] = 50
print("dictionary size:",len(m)) # 3
for k in m:
    print(k, m[k])
# Yoondy 40 Sky 100 Jerry 50

# 집합
s = set()
s.add(456)
s.add(12)
s.add(456)
s.add(7890)
s.add(7890)
s.add(456)

s.pop() # 어떤 값이 빠지는지 알 수 없음 
s.remove(12)
print("set size:",len(s))
for i in s:
    print(i)