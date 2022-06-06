"""
1717 집합의 표현
"""
import sys
sys.setrecursionlimit(500000000)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)
