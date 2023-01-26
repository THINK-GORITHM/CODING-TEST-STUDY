import sys
input = sys.stdin.readline
n, l = map(int, input().split())
spots = [False]*1001
for i in map(int, input().split()):
  spots[i] = True

ans=0
x=0
while x < 1001:
  if spots[x]:
    ans+=1
    x+=l
  else:
    x+=1 

print(ans)
