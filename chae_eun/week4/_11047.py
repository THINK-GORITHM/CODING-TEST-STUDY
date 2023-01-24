N, K = map(int, input().split())

moneyValue = [int(input()) for _ in range(N)]
count = 0
for i in reversed(moneyValue):
    count += K//i
    K=K%i

print(count)