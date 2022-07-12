import sys,math
input = sys.stdin.readline

g, l = map(int, input().split())
for i in range(math.ceil(math.sqrt(g * l)), 0, -1):
    b = g * l // i
    temp = math.gcd(i, b)
    if temp == g and i // temp * b == l:
        print(i, g * l // i)
        break