def prime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
d=0
c=0
if prime(n)==1:
    while n:
        r=n%10
        d+=1
        if prime(r)==1:
            c+=1
        n//=10
    if d==c:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")