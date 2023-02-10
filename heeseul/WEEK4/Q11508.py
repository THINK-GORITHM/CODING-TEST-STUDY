n = int(input())
c = [int(input()) for _ in range(n)]
c.sort() #오름차순 정렬
c.reverse() #내림차순 정렬
cnt = 0
price = 0
for i in c:
    cnt += 1
    if cnt == 3:
        cnt = 0
        continue
    price += i
print(price)