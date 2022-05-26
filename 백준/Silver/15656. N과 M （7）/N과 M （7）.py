n, m = map(int, input().split())
ls = sorted(map(int, input().split()))
sel = [0] * m
visited = [False] * (n + 1)

def rec(k):
	if k == m:
		print(*sel)
	else:
		for i in range(n):
			# if k == 0 or sel[k - 1] < ls[i]:
			sel[k] = ls[i]
			rec(k + 1)
			sel[k] = 0
rec(0)
