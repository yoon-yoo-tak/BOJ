"""
9205 맥주 마시면서 걸어가기
"""
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((start_x, start_y))
    while q:
        x, y = q.popleft()
        if abs(x - end_x) + abs(y - end_y) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = convi[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append((nx, ny))
                    visited[i] = True
    print('sad')
    return

t = int(input())
for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    convi = [list(map(int, input().split())) for _ in range(n)]
    end_x, end_y = map(int, input().split())
    visited = [False] * (n + 1)
    bfs()