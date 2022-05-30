"""
x * 2
x = int(str(x) + '1')
"""
from collections import deque

a, b = map(int, input().split())
res = 1
while True:
    if b == a:
        break
    elif b < a or (b % 2 != 0 and b % 10 != 1):
        res = -1
        break
    else:
        res += 1
        if b % 10 == 1:
            b //= 10
        else:
            b //= 2
print(res)