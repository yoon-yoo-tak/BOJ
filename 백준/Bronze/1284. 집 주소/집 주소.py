import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '0':
        break
    ans = 2 + len(s) - 1
    for i in s:
        if i == '1':
            ans += 2
        elif i == '0':
            ans += 4
        else:
            ans += 3
    print(ans)
