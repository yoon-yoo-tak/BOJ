import sys
input = sys.stdin.readline


for _ in range(int(input())):
    ans = int(1e10)
    n = int(input())
    mbti = list(input().split())
    if n > 32:
        print(0)
    else:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    res = 0
                    if i == j or j == k or k == i:
                        continue
                    for cchar in range(4):
                        if mbti[i][cchar] != mbti[j][cchar]:
                            res += 1
                        if mbti[j][cchar] != mbti[k][cchar]:
                            res += 1
                        if mbti[k][cchar] != mbti[i][cchar]:
                            res += 1
                    ans = min(ans, res)
        print(ans)