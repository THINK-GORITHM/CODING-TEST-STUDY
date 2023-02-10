N, L = map(int, input().split())
arrayList = list(map(int, input().split()))
arrayList.sort()

count = 1

start = arrayList[0]
for i in arrayList[1:]:
    if i in range(start, start+L): continue
    else :
        count+=1
        start = i

print(count)

# 오름 차순으로 정렬 후 
# 배열의 값이 자신의 앞 index이 값 + L에 포함 되면 continue
# 아니면 값을 더해주고(테이프를 하나 더 사용하고) 기준 위치 변경