def fact(n):
    fac=1
    while(n>1):
        fac*=n
        n-=1
    return fac    

n=int(input())
d=[0]*n
for i in range(n):
    val=int(input())
    d[i]=val
for i in d:
    print(fact(i))
    
        
        