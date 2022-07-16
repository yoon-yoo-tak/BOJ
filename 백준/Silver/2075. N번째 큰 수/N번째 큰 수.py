import sys, heapq
input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
    ls = list(map(int, input().split()))
    if q:
        for i in ls:
            if q[0] < i:
                heapq.heappush(q, i)
                heapq.heappop(q)
    else:
        for i in ls:
            heapq.heappush(q, i)
print(q[0])