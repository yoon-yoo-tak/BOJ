"""
14002
"""
import sys, math
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if ls[i] > ls[j]:
            dp[i] = max(dp[i], dp[j] + 1)
ans = []
temp = max(dp)
for i in range(n - 1, -1, -1):
    if dp[i] == temp:
        ans.append(ls[i])
        temp -= 1
print(max(dp))
print(*ans[::-1])
