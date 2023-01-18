N = int(input())

# 같은 글자면 pop 다른 글자면 push
# 서로 같은 글자를 아치형으로 그릴 때 선이 교차하면 안되기 때문
answer = 0

for i in range(N):
    array = []
    data = input()
    for j in data:
        if len(array) == 0: # 안에 값이 없으면
            array.append(j) # 넣어주고
        else: # 값이 있지만
            if array[-1] == j: # 안에 값이 같으면
                array.pop() # 빼주고
            else: array.append(j) # 아니면 다시 넣어주고
    if len(array) == 0: answer +=1

print(answer)
