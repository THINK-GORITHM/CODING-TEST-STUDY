from bisect import bisect_left, bisect_right

v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)
three = bisect_right(v, 3) - bisect_left(v, 3) # 4-2 : 3은 2개가 있다
four = bisect_right(v, 4) - bisect_left(v, 4) # 0-0: 0
six = bisect_right(v, 6) - bisect_left(v, 6) # 7-4: 3

print(f'number of 3: {three}')
print(f'number of 4: {four}')
print(f'number of 6: {six}')