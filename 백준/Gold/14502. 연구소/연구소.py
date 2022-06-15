import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline





def bfs():
    q = deque()
    visited = [[False] * m for _  in range(n)]
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                q.append((i, j))
                visited[i][j] = True
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if lab[nx][ny] != 0:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
    ans = 0
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0 and not visited[i][j]:
                ans += 1
    return ans

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
zero = [[i, j] for j in range(m) for i in range(n) if lab[i][j] == 0]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
selected = []
used = [False] * len(zero)
combi = combinations(zero, 3)

res = 0
for i in combi:
    for a, b in i:
        lab[a][b] = 1
    res = max(res, bfs())
    for a, b in i:
        lab[a][b] = 0


print(res)


