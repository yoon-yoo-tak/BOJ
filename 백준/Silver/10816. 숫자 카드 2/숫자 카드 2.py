import sys
input=sys.stdin.readline

def upper(a, l, r, x):
    result = r + 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] > x:
            result = mid
            r = mid - 1
        else:
            l = mid + 1
    return result

def lower(a, l, r, x):
    result = l - 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] < x:
            result = mid
            l = mid + 1
        else:
            r = mid - 1
    return result


n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ans = [0] * m
for i in range(m):
    ans[i] = upper(a, 0, n - 1, b[i]) - lower(a, 0, n - 1, b[i]) - 1

print(*ans)