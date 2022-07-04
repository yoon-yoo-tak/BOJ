"""
a 는 n의 약수 >> 화분 묶음으로 나눔 >> 제일 뒤에 있는 화분 a개가 가장먼저 죽음
맨 뒤에 화분들은 n // a일 마다 물을 받는다.
"""

import sys
input = sys.stdin.readline

n, k, a, b = map(int, input().split())
day = 0
while True:
    day += 1
    if not day % (n // a):
        k += b
    k -= 1
    if not k:
        break
print(day)