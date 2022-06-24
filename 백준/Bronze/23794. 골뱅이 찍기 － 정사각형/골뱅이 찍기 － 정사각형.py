import sys
input = sys.stdin.readline



n = int(input())
print('@' + '@' * n + '@')
for _ in range(n):
    print('@'+ ' ' * n  + '@')
print('@' + '@' * n + '@')
