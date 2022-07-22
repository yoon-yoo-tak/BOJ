import sys
input = sys.stdin.readline


n = int(input())
a, b, c, d, dd = [], [], [], [], {}
ans = 0
for _ in range(n):
    q = list(map(int, input().split()))
    a.append(q[0])
    b.append(q[1])
    c.append(q[2])
    d.append(q[3])

for i in a:
    for j in b:
        temp = i + j
        if temp not in dd.keys():
            dd[temp] = 1
        else:
            dd[temp] += 1

for i in c:
    for j in d:
        temp = -(i + j)  
        if temp in dd.keys(): #  0으로 만들 수 있는 경우가 존재한다.
            ans += dd[temp]
print(ans)