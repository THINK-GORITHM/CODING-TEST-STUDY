# 좋은 단어 = A와 B가 각 인접해 있는 단어
N = int(input())
result = 0
for _ in range(N):
    word = input()
    temp = []
    for i in word:
        if temp and temp[-1] == i:
            temp.pop()
        else:
            temp.append(i)
    if not temp:
        result += 1
print(result)
