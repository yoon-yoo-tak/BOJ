"""
15900 나무 탈출 (스택)
"""
import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
visited[1] = -1
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
ls = []
stack = [[1, 0]]

while stack:
    curr, l = stack.pop()
    visited[curr] = 1
    if curr != 1 and len(graph[curr]) == 1:
        ls.append(l)
        continue
    for x in graph[curr]:
        if visited[x] == 0:
            stack.append([x, l + 1])
ls = sum(ls)
print('Yes' if ls % 2 else 'No')