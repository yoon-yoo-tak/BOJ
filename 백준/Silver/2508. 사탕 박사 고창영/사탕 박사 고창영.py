"""

"""

import sys, math
input = sys.stdin.readline

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


for _ in range(int(input())):
    __ = input()
    n, m = map(int, input().split())
    box = [list(input().strip()) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if box[i][j] == 'o':
                if in_range(i, j + 1) and in_range(i, j - 1):
                    if box[i][j +1] == '<' and box[i][j - 1] == '>':
                        cnt += 1
                if in_range(i + 1, j) and in_range(i - 1, j):
                    if box[i + 1][j] == '^' and box[i - 1][j] == 'v':
                        cnt += 1
    print(cnt)