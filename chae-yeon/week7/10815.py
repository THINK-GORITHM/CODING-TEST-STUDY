from bisect import bisect_left, bisect_right

# 불필요한 정보는 _로 생략가능
_ = int(input())
cards = sorted(list(map(int, input().split())))
_ = int(input())
qry = list(map(int, input().split()))
ans = []
for q in qry:
  l = bisect_left(cards, q)
  r = bisect_right(cards, q)
  ans.append(1 if r-l else 0)

print(*ans)
# print(' '.join(map(str, ans)))
