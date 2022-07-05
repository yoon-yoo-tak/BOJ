n = 1000-int(input())
a = [500,100,50,10,5,1]
sum = 0
for coin in a:
    if coin == n:
        sum += 1
        n %= coin
    if coin < n:
        sum += n//coin
        n %= coin
print(sum)
