"""

"""

import sys, math
input = sys.stdin.readline

def calc(sx, sy, ex, ey):
    return ((sx - ex) ** 2 + (sy - ey) ** 2) ** 0.5

def dist():
    temp = calc(yumi_x, yumi_y, selected[0][0], selected[0][1])
    for i in range(len(selected) - 1):
        temp += calc(selected[i][0], selected[i][1], selected[i + 1][0], selected[i + 1][1])
    return temp

def rec(k):
    global ans
    if k == 3:
        ans = min(ans, dist())
    else:
        for i in range(3):
            if not visited[i]:
                selected.append(pos[i])
                visited[i] = True
                rec(k + 1)
                selected.pop()
                visited[i] = False


yumi_x, yumi_y = map(int, input().split())
pos = [list(map(int, input().split())) for _ in range(3)]
ans = int(1e4)
selected = []
visited = [False] * 3
rec(0)
print(int(math.floor(ans)))
