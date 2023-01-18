import sys
input = sys.stdin.readline

N = int(input())
s = []
result = []
count = 1

for i in range(N):
    num = int(input())

    while count <= num:
        s.append(count)
        result.append('+')
        count += 1

    if s[-1] == num:
        s.pop()
        result.append('-')

    else:
        print('NO')
        exit(0)

print("\n".join(result))
