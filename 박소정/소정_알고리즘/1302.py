import sys
input = sys.stdin.readline
T = int(input())

m = {}
for _ in range(T):
    title = input()
    if title in m:
        m[title] += 1
    else:
        m[title] = 1

sorted_m = sorted(m.items(), key = lambda m: (-m[1], m[0])) #키 내림차순, 값 오름차순
print(sorted_m[0][0])