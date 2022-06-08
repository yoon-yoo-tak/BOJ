import sys
from collections import Counter

input = sys.stdin.readline
n = input().strip()
num_del = input().strip()
tt = Counter(n) - Counter(num_del)
ans = ''
idx = 0
while tt:
    for i in range(9, -1, -1):
        num = str(i)
        if tt[num] < 1: # 숫자 i를 쓸 수 없다면
            continue
        pos = n.find(num, idx)
        flag = tt - Counter(n[pos:])
        if flag:
            continue
        else:
            tt[num] -= 1
            idx = pos + 1
            ans += num
            if tt[num] == 0:
                del tt[num]
            break

print(ans)