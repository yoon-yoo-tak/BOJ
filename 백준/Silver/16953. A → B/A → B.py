"""
x * 2
x = int(str(x) + '1')
"""
from collections import deque

a, b = map(int, input().split())

ans = -1
q = deque()
q.append((a, 1))

while q:
    x, cnt = q.popleft()
    if x == b:
        ans = cnt
        break
    for nx in (x * 2, int(str(x) + '1')):
        if nx < 0 or nx > b:
            continue
        q.append((nx, cnt + 1))
print(ans)