# 1836ms
import sys

input = sys.stdin.readline


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

card.sort()

for i in check:
    if binary_search(card, i, 0, n - 1) != None:
        print("1", end=' ')
    else:
        print("0", end=' ')
