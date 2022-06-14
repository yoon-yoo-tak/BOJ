import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def mult(x, y):
    if y == 1:
        return x % c
    num = mult(x, y // 2)
    if y % 2 != 0:
        return num ** 2 * x % c
    else:
        return num ** 2 % c
print(mult(a, b))