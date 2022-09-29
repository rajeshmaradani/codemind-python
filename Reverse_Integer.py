n=int(input())
rev=0
m=n
if m<0:
    n*=-1
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
if m<0:
    print(-rev)
else:
    
   print(rev)    