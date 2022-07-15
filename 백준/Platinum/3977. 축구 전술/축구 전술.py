import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e8))
input = sys.stdin.readline

def forward_dfs(x, visited, stack):
    visited[x] = 1
    for now in forward_g[x]:
        if visited[now] == 0:
            forward_dfs(now, visited, stack)
    stack.append(x)


def reverse_dfs(x, visited, stack):
    visited[x] = True
    ids[x] = idx
    stack.append(x)
    for now in reverse_g[x]:
        if not visited[now]:
            reverse_dfs(now, visited, stack)


T = int(input())
for tc in range(T):
    if tc in range(1, T):
        input()

    n, move = map(int, input().split())
    forward_g = defaultdict(list)
    reverse_g = defaultdict(list)
    for _ in range(move):
        a, b = map(int, input().split())
        forward_g[a].append(b)
        reverse_g[b].append(a)

    stack = []
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            forward_dfs(i, visited, stack)

    result = [[] for _ in range(n)]
    visited = [False] * n
    idx = -1
    ids = [-1] * n
    while stack:
        ssc = []
        x = stack.pop()
        if not visited[x]:
            idx += 1
            reverse_dfs(x, visited, ssc)
            result[idx] = ssc
    scc_indegree = [0] * (idx + 1)

    for i in range(n):
        for ed in forward_g[i]:
            if ids[i] != ids[ed]:
                scc_indegree[ids[ed]] += 1

    cnt = 0
    temp = []
    for i in range(idx + 1):
        if scc_indegree[i] == 0:
            for r in result[i]:
                temp.append(r)
            cnt += 1

    if cnt == 1:
        for i in sorted(temp):
            print(i)
    else:
        print("Confused")
    print()