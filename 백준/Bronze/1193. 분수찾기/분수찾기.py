X = int(input())
n=1
sum=1
while True:
  if sum >= X:
    if X-sum==0:
      frac_n_1 = n
      frac_n_2 = (n+1)-frac_n_1
      if n%2==0:
        print(frac_n_1,"/",frac_n_2,sep='')
        break
      else:
        print(frac_n_2,"/",frac_n_1,sep='')
        break
    else:
      frac_n_1 = X-(sum-n)
      frac_n_2 = (n+1)-frac_n_1
      if n%2==0:
        print(frac_n_1,"/",frac_n_2, sep='')
        break
      else:
        print(frac_n_2,"/",frac_n_1, sep='')
        break
  n+=1
  sum+=n