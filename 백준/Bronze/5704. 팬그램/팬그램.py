"""
5704 팬그램
"""
import sys

input = sys.stdin.readline

while True:
    s = input().split()
    if s[0] == '*':
        break
    ls = [0] * 26
    for i in s:
        for j in i:
            ls[ord(j) - 97] += 1
    ans = 'Y'
    for i in ls:
        if i == 0:
            ans = 'N'
            break
    print(ans)