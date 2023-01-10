import sys
n=int(sys.stdin.readline())
d={}
res=[]
for _ in range(n):
  m=sys.stdin.readline()
  if m in d:
    d[m]+=1
  else:
    d[m]=1


num=max(d.values())
for i in d:
  if d[i]==num:
    res.append(i)

res.sort()
print(res[0])