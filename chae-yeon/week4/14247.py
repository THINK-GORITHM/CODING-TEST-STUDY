import sys
n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
grow = list(map(int, sys.stdin.readline().split()))
arr=[]
ans=0
for i in range(n):
  arr.append([tree[i],grow[i]])

arr=sorted(arr, key=lambda x: [x[1]])

for i in range(n):
  ans+=arr[i][0] + (i*arr[i][1])

print(ans)