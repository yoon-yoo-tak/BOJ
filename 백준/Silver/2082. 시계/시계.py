"""

"""

import sys, math
input = sys.stdin.readline

nums = [
'####.##.##.####',
 '..#..#..#..#..#',
 '###..#####..###',
 '###..####..####',
 '#.##.####..#..#',
 '####..###..####',
 '####..####.####',
 '###..#..#..#..#',
 '####.#####.####',
 '####.####..####'
]

time = ['' for _ in range(4)]

for _ in range(5):
    k = input().split()
    for i in range(4):
        time[i] += k[i]

ans = []

for t in time:
    num = [[0, i] for i in range(10)]
    for i in range(10):
        for j in range(15):
            if t[j] == '#' and nums[i][j] == '.':
                num[i][0] = 1
                break
    num_sorted = sorted(num, key=lambda x: (x[0], x[1]))
    ans.append(num_sorted[0][1])

for i in range(4):
    print(ans[i], end='')
    if i == 1:
        print(':', end='')