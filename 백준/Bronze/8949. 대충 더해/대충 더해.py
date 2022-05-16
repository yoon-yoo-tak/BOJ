"""
8949 대충 더해

"""

import sys

input = sys.stdin.readline

a, b = list(input().split())
len_diff = abs(len(a) - len(b))
if len(a) >= len(b):
    b = '0' * len_diff + b
else:
    a = '0' * len_diff + a
ans = ''
for i in range(len(a)):
    ans += str(int(a[i]) + int(b[i]))
print(ans)