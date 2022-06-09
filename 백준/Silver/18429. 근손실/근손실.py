from itertools import permutations
import sys
n, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

answer = 0
for data in permutations(array, n):
    weight = 500
    flag = True
    for i in range(n):
        weight += data[i]
        weight -= k
        if weight < 500:
            flag = False
            break
    if flag:
        answer += 1

print(answer)
