n, m = map(int, input().split())

selected = [0] * m
visited = [False] * (n + 1)
def rec(x):
    if x == m:
        print(*selected)
        return
    else:
        for i in range(1, n + 1):
            if visited[i]:
                continue
            selected[x] = i
            visited[i] = True
            rec(x + 1)
            selected[x] = 0
            visited[i] = False

rec(0)