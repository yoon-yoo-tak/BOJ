import sys
input = sys.stdin.readline


n = int(input())
ls = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1], reverse=True)
time = ls[0][1] - ls[0][0] + 1

for i in range(1, len(ls)):
    if ls[i][1] >= time:
        time = ls[i][1] - ls[i][0] - (ls[i][1] - time)
    else:
        time = ls[i][1] - ls[i][0] + 1
print(time - 1)