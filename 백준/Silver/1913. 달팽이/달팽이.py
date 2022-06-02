import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n = int(input())
target = int(input())
graph = [[0] * n for _ in range(n)]
graph[0][0] = n ** 2
x, y = 0, 0
idx = 0
while True:
    if idx == 4:
        idx = 0
    nx, ny = x + dx[idx], y + dy[idx]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        idx += 1
        continue
    if graph[nx][ny] != 0:
        idx += 1
        continue
    graph[nx][ny] = graph[x][y] - 1
    x, y = nx, ny
    if graph[nx][ny] == 1:
        break

for i in range(n):
    for j in range(n):
        if graph[i][j] == target:
            sx, sy = i + 1 , j + 1

for i in graph:
    print(*i)
print(sx, sy)

