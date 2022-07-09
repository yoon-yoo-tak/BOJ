a, b = map(int, input().split())
res = a - a * b / 100
print(1 if res < 100 else 0)