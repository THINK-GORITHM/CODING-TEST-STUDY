import sys

# Ai는 Ai-1의 배수라는 말이 있으므로 그리디로 접근할 수 있다.

n, k = map(int, sys.stdin.readline().split());
coins = [int(sys.stdin.readline())for _ in range(n)]
coins.reverse()
ans = 0
for coin in coins:
  ans += k//coin
  k%=coin

print(ans)