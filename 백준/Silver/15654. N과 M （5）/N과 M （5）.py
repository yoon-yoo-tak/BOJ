n, m = map(int, input().split())
ls = sorted(map(int, input().split()))
sel = [0] * m
visited = [False] * (n + 1)

def rec(k):
	if k == m:
		print(*sel)
	else:
		# start = 1 if k == 0 else sel[k -1]
		for i in range(n):
			if not visited[i]:
				sel[k] = ls[i]
				visited[i] = True
				rec(k + 1)
				sel[k] = 0
				visited[i] = False
rec(0)
