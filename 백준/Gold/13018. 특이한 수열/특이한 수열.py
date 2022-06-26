n,k=map(int,input().split())
if k==n:print('Impossible')
else:print(*[i for i in range(2,(n-k)+1)]+[1],*[j for j in range((n-k)+1,n+1)])