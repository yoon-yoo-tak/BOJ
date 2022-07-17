T = int(input())

for tt in range(1, T + 1):
    n = int(input())
    ans = ''
    while n > 0:
        a, b = input().split()
        ans += a * int(b)
        n -= 1
    print(f'#{tt}')
    for i in range(1, len(ans) // 10 + 1):
        last = i * 10
        print(ans[last - 10:last])
    print(ans[-(len(ans) % 10):])


