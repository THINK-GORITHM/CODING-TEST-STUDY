N = int(input())
tree = dict()
for _ in range(N):
    n, l, r = input().rstrip().split()
    tree[n] = (l, r) #key : 노드, value : (왼쪽자식, 오른쪽자식)

#전위 (루트-왼-오른)
def preorder(n, result):
    result += n     #루트 추가
    for i in tree[n]:   #루트의 왼쪽, 오른쪽 자식
        if i == ".":    #자식이 없다면
            continue    #다음 노드로 넘어가기
        result = preorder(i, result)     #자식이 있다면 그 자식에 대해 반복해줌
    return result

#중위 (왼-루트-오른)
def inorder(n, result):
    if n == ".":    #루트가 없는 경우
        return result
    l, r = tree[n]      #l:왼쪽자식, r:오른쪽자식
    result = inorder(l, result)     #왼쪽자식 먼저 순회
    result += n     #왼쪽자식 순회 결과에 루트 추가
    result = inorder(r, result)     #오른쪽자식 순회
    return result

#후위 (왼-오른-루트)
def postorder(n, result):
    if tree[n] == (".", "."): #왼/오른쪽 자식이 둘 다 없는 경우
        return result + n
    for i in tree[n]:
        if i == ".":    #자식이 없는 경우
            continue
        result = postorder(i, result)   #자식이 존재하면 순회하고 결과 반영
    return result + n   #마지막에 루트 추가

print(preorder("A", ""))
print(inorder("A", ""))
print(postorder("A", ""))
