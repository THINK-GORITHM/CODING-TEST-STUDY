d = dict()

for _ in range(int(input())):
    book = input()
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

m = max(d.values())
c = []
for k, v in d.items():
    if v == m:
        c.append(k)
c.sort()
print(c[0])
