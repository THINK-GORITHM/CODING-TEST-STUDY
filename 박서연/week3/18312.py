# 96ms
import sys

n, k = map(int, sys.stdin.readline().split())
num = 0

for i in range(n+1):
    if i < 10:
        i = '0'+str(i)
    for j in range(60):
        if j < 10:
            j = '0'+str(j)
        for z in range(60):
            if z < 10:
                z = '0'+str(z)
            if str(k) in str(i)+str(j)+str(z):
                num += 1
print(num)
