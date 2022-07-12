import sys,math
input = sys.stdin.readline

def make():
    global ls
    ls = [0] * 1001
    ls[1] = 3
    for i in range(2, 1001):
        cnt = 0
        for j in range(1, i + 1):
            if i == j:
                continue
            if math.gcd(i, j) == 1:
                cnt += 2
        ls[i] = ls[i - 1] + cnt

ls = []
make()
for _ in range(int(input())):
    print(ls[int(input())])