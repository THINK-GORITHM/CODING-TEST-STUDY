import sys

N = int(sys.stdin.readline())
# tree 생성
tree = {}  # Dictionary
for _ in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]


def preorder(alpa):
    if alpa == '.':
        return
    print(alpa, end="")
    preorder(tree[alpa][0])
    preorder(tree[alpa][1])


def inorder(alpa):
    if alpa == '.':
        return
    inorder(tree[alpa][0])
    print(alpa, end="")
    inorder(tree[alpa][1])


def postorder(alpa):
    if alpa == '.':
        return
    postorder(tree[alpa][0])
    postorder(tree[alpa][1])
    print(alpa, end="")


preorder('A')
print()
inorder('A')
print()
postorder('A')
