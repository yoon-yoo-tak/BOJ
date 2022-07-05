import sys
input = sys.stdin.readline

month = [0, 31, 28,31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["Wednesday", "Thursday",
       "Friday", "Saturday", "Sunday","Monday", "Tuesday"]


d, m = map(int, input().split())

print(day[(sum(month[:m]) + d) % 7])

