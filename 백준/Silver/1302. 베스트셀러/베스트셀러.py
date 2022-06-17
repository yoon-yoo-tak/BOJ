n = int(input())
book = {}
for _ in range(n):
    s = input()
    if s in book:
        book[s] += 1
    else:
        book[s] = 1
ls = sorted([[i, book[i]] for i in book], key=lambda x:(-x[1], x[0]))
print(ls[0][0])