import heapq as hq
import sys

n=int(sys.stdin.readline())

q=[]

for _ in range(n):
  m=int(sys.stdin.readline())
  if m !=0:
    # heap을 tuple로 구성했을 때 맨 앞 숫자만으로 정렬을 하므로 절댓값 정렬이 가능
    hq.heappush(q, (abs(m),m))
  else:
    if len(q)==0:
      print(0)
    else:
      print(hq.heappop(q)[1])


