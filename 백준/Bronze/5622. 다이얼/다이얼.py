import sys
input = sys.stdin.readline

cnt = '22233344455566677778889999'
ans = 0
for i in input().strip():
    ans += int(cnt[ord(i) - 65]) + 1
print(ans)
