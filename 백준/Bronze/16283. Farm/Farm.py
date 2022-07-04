import sys
input = sys.stdin.readline


a, b, n, w = map(int, input().split())
sheep = []
goat = []

for i in range(1, 1000):
    for j in range(1, 1000):
        if a * i + j * b == w:
            if i + j == n:
                sheep.append(i)
                goat.append(j)
if not sheep and not goat:
    print(-1)
elif len(sheep) + len(goat) > 2:
    print(-1)
else:
    print(*sheep, *goat)
