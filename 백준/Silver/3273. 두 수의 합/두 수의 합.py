import sys
input=sys.stdin.readline


def bisect(a, l, r, x):
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return True
        if a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False


ans = 0
n = int(input())
a = sorted(map(int, input().split()))
x = int(input())

for i in range(n):
    target = x - a[i]
    if bisect(a, i + 1, n - 1, target):
        ans += 1

print(ans)