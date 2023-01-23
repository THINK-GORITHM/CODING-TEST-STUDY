from itertools import combinations

# arr = []
# for _ in range(9):
#     arr.append(int(input()))

arr = [int(input()) for _ in range(9)]

for i in combinations(arr, 7):
    if sum(i) == 100:
        for j in  sorted(i):
            print(j)
        break # 답이 여러가지 나올 수 있지만 1개만 출력해야함