n=int(input())
t=n*n
sum=0
while(t):
    r=t%10
    sum=sum+r
    t//=10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")