"""

"""

import sys
input = sys.stdin.readline
*a, n = map(int, input().split())
ra = n // a[0] + 1
for i in range(ra):
    for j in range(ra):
        for k in range(ra):
            if i * a[0] + j * a[1] + k * a[2] == n:
                print(1)
                sys.exit()
print(0)

