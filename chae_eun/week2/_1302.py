# data structure map 사용
n = int(input())
array = {}
for i in range(n):
    books = input()
    if books not in array: array[books] = 1
    else : array[books] += 1

lists = sorted(array.items(), key=lambda x: (-x[1], x[0]))
print(lists[0][0])