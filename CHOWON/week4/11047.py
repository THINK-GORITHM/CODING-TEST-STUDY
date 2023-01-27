n, k = map(int, input().split())

coins = list()

for _ in range(n):
    coins.append(int(input()))

coins.reverse()
result = 0
for coin in coins:
    result += k//coin
    k %= coin

print(result)