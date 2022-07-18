import sys
input = sys.stdin.readline
INF = sys.maxsize
v, e = map(int, input().split())
graph = [[INF] * v for _ in range(v)]

for _ in range(e):
    i, j, c = map(int, input().split())
    graph[i - 1][j - 1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = INF

for i in range(v):
    ans = min(ans, graph[i][i])
print(-1 if ans == INF else ans)

