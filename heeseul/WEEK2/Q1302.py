dic = dict()

for _ in range(int(input())):
    book = input()
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1

m = max(dic.values())
c = []
for k, v in dic.items():
    if v == m:
        c.append(k)
c.sort()
print(c[0])
