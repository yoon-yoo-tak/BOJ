import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '#':
        break
    cnt = 0
    for i in s:
        if i in 'aeiouAEIOU':
            cnt += 1
    print(cnt)
