N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
result = 0

while K != 0:
    for c in reversed(coin):
        result += K // c
        K = K % c

print(result)
