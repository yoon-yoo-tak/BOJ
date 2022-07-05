import sys
input = sys.stdin.readline

gan = [1,2,3,3,4,10]
ron = [1,2,2,2,3,5,10]

for tt in range(1, int(input()) + 1):
    ans = ''
    gan_score = sum([i * j for i, j in zip(gan, list(map(int, input().split())))])
    ron_score = sum([i * j for i, j in zip(ron, list(map(int, input().split())))])
    if gan_score > ron_score:
        ans = 'Good triumphs over Evil'
    elif gan_score < ron_score:
        ans = 'Evil eradicates all trace of Good'
    else:
        ans = 'No victor on this battle field'
    print(f'Battle {tt}: {ans}')