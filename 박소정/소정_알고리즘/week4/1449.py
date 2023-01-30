N, L = map(int, input().split())
leak = list(map(int, input().split()))
leak.sort()

result = 0
point = 0 # 테이프 붙인 위치

for i in leak:
    if point < i:
        result += 1
        point = i+L-1 # 물 새는 곳 + 테이프 길이 -1(새는 곳부터 count) = 테이프 붙인 위치

print(result)
