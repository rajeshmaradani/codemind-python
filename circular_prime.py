def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
def reve(n):
    rev=0
    while(n>0):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev    
        
n=int(input())
m=reve(n)
if prime(n)==1 and prime(m)==1:
    print("circular prime")
elif prime(n)!=1:
    print("not prime")
else:
    print("prime but not a circular prime")

