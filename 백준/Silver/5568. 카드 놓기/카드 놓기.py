n = int(input())
k = int(input())
ls = [input() for _ in range(n)]
ans = set()
selected = []
visited = [False] * n
def rec(x):
    if x == k:
        ans.add(int(''.join(selected)))
        return
    else:
        for i in range(n):
            if not visited[i]:
                selected.append(ls[i])
                visited[i] = True
                rec(x + 1)
                selected.pop()
                visited[i] = False
rec(0)
print(len(ans))