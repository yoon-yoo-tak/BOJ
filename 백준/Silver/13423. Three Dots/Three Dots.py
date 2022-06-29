"""
13423 Tree Dots
N^3 안됨
N^2 가능 > 2개 정하고 나머지 하나 찾기
"""

import sys
input = sys.stdin.readline

def bisect(a, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if ls[mid] == x:
            return True
        if ls[mid] <= x:
            l = mid + 1
        else:
            r = mid - 1
    return False


for _ in range(int(input())):
    n = int(input())
    ls = sorted(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ab = abs(ls[j] - ls[i])
            if bisect(ls, 0, n - 1, ab + ls[j]):
                ans += 1
    print(ans)