from collections import deque

def bfs(x ,y):
    q = deque()
    q.append((x, y))
    dist[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '1' and dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
bfs(0, 0)
print(dist[n - 1][m - 1])