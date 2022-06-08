import sys
input = sys.stdin.readline


n, m = map(int, input().split())

selected = [0] * m

def rec(k):
    if k == m:  # m 개 뽑았다!
        print(*selected)
    else:
        start = 1 if k == 0 else selected[k - 1]
        for i in range(start, n + 1):
            selected[k] = i
            rec(k + 1)
            selected[k] = 0

rec(0)