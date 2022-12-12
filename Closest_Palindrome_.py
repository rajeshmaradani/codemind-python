def polin(n):
    t=n
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n//=10
    if t==rev:
        return 1
    else:
        return 0
n=int(input())
for i in range(n+1,n**10,1):
    if polin(i)==1:
        m=i
        break
for i in range(n-1,0,-1):
    if polin(i)==1:
        m1=i
        break
n1=n-m1
n2=m-n
if n1>n2:
    print(m)
elif n1<n2:
    print(m1)
else:
    print(m1,m)
        