n = int(input())
Hi = list(map(int, input().split()))
Ai = list(map(int, input().split()))
total = 0
tree = [] #나무의 길이와 자라는 길이를 담을 리스트
for i in range(n):
    tree.append((Ai[i], Hi[i]))
tree.sort()
for j in range(n):
    total += tree[j][1] + tree[j][0] * j #나무의 길이 + 자란 나무 길이(나무의 성장속도 * 날)
print(total)