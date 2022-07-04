"""

"""

import sys
input = sys.stdin.readline

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
far = 0
for i in range(1, n - 1):
    temp = (abs(ls[i + 1][0] - ls[i][0]) + abs(ls[i + 1][1] - ls[i][1]) + abs(ls[i][0] - ls[i - 1][0]) + abs(ls[i][1] - ls[i - 1][1])) - (abs(ls[i + 1][0] - ls[i - 1][0]) + abs(ls[i + 1][1] - ls[i - 1][1]))
    far = max(temp, far)
x = ls[0][0]
y = ls[0][1]
ans = 0
for i in range(1, n):
    ans += (abs(ls[i][0] - x) + abs(ls[i][1] - y))
    x = ls[i][0]
    y = ls[i][1]
print(ans - far)