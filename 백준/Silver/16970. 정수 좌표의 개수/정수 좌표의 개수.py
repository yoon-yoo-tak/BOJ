import sys,math
input = sys.stdin.readline

n, m, k = map(int, input().split())
n, m = n + 1, m + 1
ans = 0
for i in range(n):
    for j in range(m):
        for p in range(n):
            for q in range(m):
                if math.gcd(p - i, q - j) == k - 1: ans += 1
print(ans // 2)