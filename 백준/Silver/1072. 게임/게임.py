"""
1072 게임
"""
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = (y * 100 // x)

if z >= 99: # 판수 아무리 때려박아도 안바뀜
    print(-1)
else:
    cnt = 0
    l, r = 1, x
    while l <= r:
        mid = (l + r) // 2
        if ((mid + y) * 100) // (mid + x) <= z:
            l = mid + 1
        else:
            cnt = mid
            r = mid - 1

    print(cnt)
