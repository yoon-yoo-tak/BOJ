
n = int(input())
cow = dict()
cnt = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a in cow.keys():
        if cow[a] != b:
            cnt += 1
            cow[a] = b
    else:
        cow[a] = b
print(cnt)