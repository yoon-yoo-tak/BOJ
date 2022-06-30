import sys
input = sys.stdin.readline

n = int(input())
ls = sorted(map(int, input().split()))
ans = 0
if n % 2: # 홀수면 마지막꺼 빼놓고
    last = ls.pop()
for i in range(n // 2):
    ans = max(ans, ls[i] + ls[-i - 1])  # 처음, 끝 합 비교
print(max(ans, last) if n % 2 else ans)