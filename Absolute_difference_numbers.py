def rev(n):
    s=0
    while n:
        r=n%10
        s=s*10+r
        n//=10
    return s    



n,x=map(int,input().split())
r=n%10**x
p=rev(n)
s=0
for i in range(1,x+1):
    r1=p%10
    s=s*10+r1
    p//=10
print(abs(r-s))
