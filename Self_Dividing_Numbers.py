def add(n):
    t=n
    f=0
    c=0
    while n:
        r=n%10
        c+=1
        if r!=0 and t%r==0:
            f+=1
        n=n//10
    if f==c:
        return t
    else:
        return 0
a=int(input())
b=int(input())
for i in range(a,b+1):
    dc=add(i)
    if(dc!=0):
         print(dc,end=" ")
            