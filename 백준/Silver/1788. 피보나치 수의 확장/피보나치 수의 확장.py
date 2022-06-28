"""
피보나치 수의 확장
"""
import sys
input = sys.stdin.readline
MOD = 1000000000
dp = [0] * 1000001
dp[0] = 0
dp[1] = 1

n = int(input())
if n > 0:
    sign = 1
elif n == 0:
    sign = 0
else:
    sign = -1

for i in range(2, abs(n) + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

if sign == -1 and -n % 2 != 0:
    sign *= -1

print(sign)
print(dp[abs(n)])