def prime(n):
    if n==1:
        return 0
    for i in range(2,n):
        if (n%i==0):
            return 0
    return n        
m=int(input())
n=int(input())
for i in range (m,n+1):
    c=prime(i)
    if c!=0:
        print(c)