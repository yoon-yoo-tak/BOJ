import sys
input = sys.stdin.readline

keypad = [[], ['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L']
          ,['M','N','O'],['P','Q','R','S'], ['T','U','V'], ['W','X','Y','Z']]

p, w = map(int, input().split())
message = input().strip()

ans = 0
last = ''
for i in range(len(message)):
    if message[i] == ' ':
        ans += p
        last = ''
    for j in range(len(keypad)):
        for k in range(len(keypad[j])):
            if message[i] == keypad[j][k]:
                if j == last:
                    ans += w
                ans += (k + 1) * p
                last = j
print(ans)