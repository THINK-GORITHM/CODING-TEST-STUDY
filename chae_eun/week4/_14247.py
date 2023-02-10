# 가장 자라나는 속도가 높은 나무는 마지막에 자르기
N = int(input()) # 나무의 개수
first = list(map(int, input().split())) # 처음 나무 길이
lengthT = list(map(int, input().split())) # 나무 자라나는 길이

array = [[first[i], lengthT[i]] for i in range(N)]
array = sorted(array, key = lambda x: (x[1]))   
count = 0
for i in range(N):
    count += array[i][0] +  array[i][1] * i

print(count)