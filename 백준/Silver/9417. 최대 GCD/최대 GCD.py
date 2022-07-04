"""

"""

import sys, math
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    ls = list(map(int, input().split()))
    ans = 0
    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            ans = max(ans, math.gcd(ls[i], ls[j]))
    print(ans)