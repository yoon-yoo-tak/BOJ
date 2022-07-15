"""
2150 Strongly Connected Component
코-사라주
"""
import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def forward_dfs(x):
    visited.add(x)
    for next in forward_g[x]:
        if next not in visited:
            forward_dfs(next)
    stack.append(x)

def reverse_dfs(x, scc):
    visited.add(x)
    scc.append(x)
    for next in reverse_g[x]:
        if next not in visited:
            scc = reverse_dfs(next, scc)
    return scc

def kosaraju():
    global visited
    answer = []
    for i in range(1, v + 1):
        if i not in visited:
            forward_dfs(i)
    visited = set() # 초기화
    while stack:
        scc = []
        x = stack.pop()
        if x in visited:
            continue
        answer.append(sorted(reverse_dfs(x, scc)))
    return answer


v, e = map(int, input().split())
forward_g = defaultdict(list)
reverse_g = defaultdict(list)
for _ in range(e):
    a, b = map(int, input().split())
    forward_g[a].append(b)
    reverse_g[b].append(a)

stack = []
visited = set()
answer = kosaraju()

print(len(answer))
for i in sorted(answer):
    print(*i,end=' -1\n')