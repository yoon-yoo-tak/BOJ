import sys
input = sys.stdin.readline

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]

ans = [int(1e10) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        dist = sorted([abs(ls[i][0] - ls[k][0]) + abs(ls[j][1] - ls[k][1]) for k in range(n)])
        temp = 0
        for k in range(n):
            temp += dist[k]
            ans[k + 1] = min(ans[k + 1], temp)
print(*ans[1:])
