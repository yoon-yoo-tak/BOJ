"""

"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]
ans = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            ans[i][j] += ls[i][l] * B[l][j]
for i in ans:
    print(*i)
