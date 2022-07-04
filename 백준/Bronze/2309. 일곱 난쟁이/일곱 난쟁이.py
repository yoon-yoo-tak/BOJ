import sys
input = sys.stdin.readline

ls = sorted(int(input()) for _ in range(9))
total = sum(ls)
target = 100
flag = False
for i in range(8):
    for j in range(i + 1, 9):
        if total - ls[i] - ls[j] == 100:
           num1 = ls[i]
           num2 = ls[j]
           flag = True
           break
    if flag:
        break
for i in ls:
    if i == num1 or i == num2:
        continue
    print(i)