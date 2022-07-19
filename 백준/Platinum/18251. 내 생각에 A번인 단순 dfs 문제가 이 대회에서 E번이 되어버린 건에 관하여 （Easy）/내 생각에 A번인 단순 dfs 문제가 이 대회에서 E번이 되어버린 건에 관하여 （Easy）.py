import sys, math
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n = int(input().strip())
vertex = list(map(int, input().split()))
tree = []
height = int(math.log2(n)) + 1


def in_order(index, x, h):  # 중위 순회
    if index * 2 <= n:
        x = in_order(index * 2, x, h + 1)
    tree.append([x, h, vertex[index - 1]])
    if index * 2 + 1 <= n:
        x = in_order(index * 2 + 1, x + 1, h + 1)
    return x + 1


in_order(1, 0, 0)
ans = tree[0][2]
for i in range(height):
    for j in range(i, height):
        s = 0
        for n in tree:
            if n[1] < i or j < n[1]:
                continue
            if s + n[2] >= 0:
                s += n[2]
                ans = max(ans, s)
            else:
                ans = max(ans, n[2])
                s = 0
print(ans)