n, m = map(int, input().split())

sel = [0 for _ in range(m)]

def rec_func(k):
    if k == m:
        for x in sel:
            print(x, end=' ')
        print()
    else:
        start = 1 if k == 0 else sel[k-1]+1
        for i in range(start, n+1):
            sel[k] = i
            rec_func(k+1)
            sel[k] = 0

rec_func(0)