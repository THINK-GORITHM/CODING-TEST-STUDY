import sys
input = sys.stdin.readline

N = int(input())
firstLength = list(map(int, input().split()))
growLength = list(map(int, input().split()))
tree = []
result = 0

for i in range(N):
    tree.append((firstLength[i], growLength[i]))

tree.sort(key = lambda x:x[1])

for i in range(N):
    result += tree[i][0] + tree[i][1] * i

print(result)