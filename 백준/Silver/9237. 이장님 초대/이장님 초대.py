import sys
input = sys.stdin.readline

n = int(input())
tree = sorted(map(int, input().split()), reverse=True)
print(max([tree[i] + i + 1 for i in range(len(tree))]) + 1)
