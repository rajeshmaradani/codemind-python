def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
n=int(input())
l=len(str(n))
t=n
c=0
if prime(n)==1:
    while n:
        r=n%10
        if prime(r)==1:
            c=c+1
        n=n//10
    if c==l:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
    