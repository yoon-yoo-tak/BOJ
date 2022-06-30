import sys
input = sys.stdin.readline


def valid(num):
    temp = 0
    for i in range(n):
        if temp > num:
            return False
        temp += ls[i]
        if temp == num:
            temp = 0
    return True

for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    cnt = ls.count(0)
    ans = 0
    start = max(1, max(ls))
    prefix_sum = [0] * n
    prefix_sum[0] = ls[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + ls[i]
    for i in range(start, prefix_sum[-1] + 1):
        if not prefix_sum[-1] % i and valid(i):
            ans = n - (prefix_sum[-1] // i)
            break
    print(ans)