n, m= map(int, input().split())
nums = sorted(map(int, input().split()))

sel = [0 for _ in range(m)]
used = [0 for _ in range(n+1)]
def rec(k):
    if k == m:
        for x in sel:
            print(x, end=' ')
        print()
    else:
        for cand in range(n):
            if k==0 or sel[k-1] < nums[cand]:
                sel[k] = nums[cand]
                rec(k + 1)
                sel[k] = 0

rec(0)