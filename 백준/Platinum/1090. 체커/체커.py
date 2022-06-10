"""
체커
"""
import sys
input = sys.stdin.readline

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
a = [int(sys.maxsize) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        x, y = ls[i][0], ls[j][1]
        dist = sorted([abs(x - ls[k][0]) + abs(y - ls[k][1]) for k in range(n)])
        total = 0
        for k in range(n):
            total += dist[k]
            a[k + 1] = min(a[k + 1], total)
print(*a[1:])