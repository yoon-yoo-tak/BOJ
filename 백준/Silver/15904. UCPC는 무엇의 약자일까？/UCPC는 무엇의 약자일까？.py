import sys
input = sys.stdin.readline


s = input().strip()
ucpc = 'UCPC'
flag = True

for i in range(4):
    if ucpc[i] in s:
        flag = True
        idx = s.find(ucpc[i])
        s = s[idx + 1:]
    else:
        flag = False
        break
print('I love UCPC' if flag else 'I hate UCPC')