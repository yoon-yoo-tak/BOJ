"""

"""

import sys, math
input = sys.stdin.readline
x = int(input())
flag = True
if x == 0:
    print('NO')
    sys.exit()
while True:
    if x == 0:
        break
    if x % 3 > 1:
        flag = False
        break
    x //= 3
print('YES' if flag else 'NO')