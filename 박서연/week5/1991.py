# 전위 순회(preorder traverse) : 뿌리(root)를 먼저 방문
# 중위 순회(inorder traverse) : 왼쪽 하위 트리를 방문 후 뿌리(root)를 방문
# 후위 순회(postorder traverse) : 하위 트리 모두 방문 후 뿌리(root)를 방문
# 40ms
import sys


def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])


def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])


def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


input = sys.stdin.readline
n = int(input())
tree = {}

for i in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
