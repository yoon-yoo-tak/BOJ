"""

"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(map(int, input().split()))
for i in range(1, n):
    ls[i] = ls[i - 1] + ls[i]
ans = -int(1e5)
for i in range(n - k + 1):
    if i == 0:
        ans = max(ans, ls[k - 1])
    else:
        ans = max(ans, ls[i + k - 1] - ls[i - 1])
print(ans)
