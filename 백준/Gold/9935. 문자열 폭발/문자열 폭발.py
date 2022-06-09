s = input()
bomb = input()

last = bomb[-1]
ls = []
n = len(bomb)

for i in s:
    ls.append(i)
    if i == last and ''.join(ls[-n:]) == bomb:
        del ls[-n:]
ans = ''.join(ls)
print(ans if len(ans) > 0 else 'FRULA')