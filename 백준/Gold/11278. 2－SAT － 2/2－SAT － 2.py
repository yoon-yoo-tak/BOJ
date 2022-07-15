import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e8))
input = sys.stdin.readline

n, m = map(int, input().split())
jul = []

for i in range(m):
    a, b = map(int, input().split())
    jul.append((a, b))


def make(word):
    if len(word) == n + 1:
        sat(word)
        return
    for i in range(2):
        make(word + [i])


def sat(to_check):
    for xi, xj in jul:
        jul1 = to_check[xi] if xi > 0 else not to_check[-xi]
        jul2 = to_check[xj] if xj > 0 else not to_check[-xj]
        if (jul1 or jul2) == 0:
            return
    print(1)
    for i in range(1, n + 1):
        print(to_check[i], end=' ')
    exit()


make([''])
print(0)