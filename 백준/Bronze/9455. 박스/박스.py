import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = 0
    ls = [list(map(int, input().split())) for _ in range(n)]
    ls = ls[::-1]
    new_ls = [[] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_ls[i].append(ls[j][i])

    ans = 0
    for i in new_ls:
        one_cnt = i.count(1)
        one_pos = [j for j in range(len(i)) if i[j] == 1]
        if one_cnt <= 1:
            ans += sum(one_pos)
        else:
            ans += one_pos[0]
            for j in range(1, len(one_pos)):
                ans += one_pos[j] - j
    print(ans)