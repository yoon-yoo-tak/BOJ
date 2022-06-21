import sys
input=sys.stdin.readline

n = int(input())
ls = [input().strip() for _ in range(n)]
print(len(set([''.join(sorted(i)) for i in ls])))