"""
8949 대충 더해

"""

import sys

input = sys.stdin.readline

a, b = input().split()
a = a[::-1]
b = b[::-1]
ans = []
if len(a) >= len(b):
    for i in range(len(b)):
        ans.append(str(int(a[i]) + int(b[i])))
    ans += a[len(b):]
else:
    for i in range(len(a)):
        ans.append(str(int(a[i]) + int(b[i])))
    ans += b[len(a):]
ans.reverse()
print(''.join(ans))