import sys
from collections import defaultdict
input = sys.stdin.readline

def check(x):
    ch = [False] * 10
    while x:
        temp = x % 10
        if ch[temp]:
            return False
        ch[temp] = True
        x //= 10
    return True

ans = [0] * 1000001
index = 1
num = 0

while True:
    num += 1
    if check(num):
        ans[index] = num
        index += 1
    if index == 1000001:
        break

while True:
    n = int(input())
    if n == 0:
        break
    print(ans[n])



