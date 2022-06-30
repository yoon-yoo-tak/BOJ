import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0
prefix_sum = [[0] * n for _ in range(n)]
area_up = []
area_down = []


def left_down(x, y):
    for i in range(x, n):
        temp = 0
        for j in range(y, -1, -1):
            temp += graph[i][j]
            if i == x:
                prefix_sum[i][j] = temp
            else:
                prefix_sum[i][j] = prefix_sum[i -1][j] + temp
            area_down.append(prefix_sum[i][j])

def right_up(x, y):
    for i in range(x, -1, -1):
        temp = 0
        for j in range(y, n):
            temp += graph[i][j]
            if i == x:
                prefix_sum[i][j] = temp
            else:
                prefix_sum[i][j] = prefix_sum[i + 1][j] + temp
            area_up.append(prefix_sum[i][j])

def right_down(x, y):
    for i in range(x, n):
        temp = 0
        for j in range(y, n):
            temp += graph[i][j]
            if i == x:
                prefix_sum[i][j] = temp
            else:
                prefix_sum[i][j] = prefix_sum[i - 1][j] + temp
            area_down.append(prefix_sum[i][j])

def left_up(x, y):
    for i in range(x, -1, -1):
        temp = 0
        for j in range(y, -1, -1):
            temp += graph[i][j]
            if i == x:
                prefix_sum[i][j] = temp
            else:
                prefix_sum[i][j] = prefix_sum[i + 1][j] + temp
            area_up.append(prefix_sum[i][j])

def calc():
    global ans
    for i in area_up:
        for j in area_down:
            if i == j:
                ans += 1

for i in range(n - 1):
    for j in range(n - 1):
        left_up(i, j)
        right_down(i + 1, j + 1)
        calc()
        prefix_sum = [[0] * n for _ in range(n)]
        area_up = []
        area_down = []

        right_up(i, j + 1)
        left_down(i + 1, j)
        calc()
        prefix_sum = [[0] * n for _ in range(n)]
        area_up = []
        area_down = []

print(ans)