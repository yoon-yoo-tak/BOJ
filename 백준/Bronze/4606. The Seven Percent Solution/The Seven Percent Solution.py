import sys
input = sys.stdin.readline


character = [' ', '!', '$', '%', '(', ')', '*']
encoding = ['%20', '%21', '%24', '%25' ,'%28', '%29', '%2a']



while True:
    s = input().strip()
    if s == '#':
        break
    ans = ''
    for i in range(len(s)):
        temp = False
        for j in range(7):
            if s[i] == character[j]:
                ans += encoding[j]
                temp = True
                break
        if not temp:
            ans += s[i]
    print(ans)
