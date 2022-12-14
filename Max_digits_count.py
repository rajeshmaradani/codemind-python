def count(n):
    c=0
    while n:
        r=n%10
        c+=1
        n//=10
    return c
n=int(input())
r=[]
c=0
x=list(map(int,input().split()))
for i in x:
    r.append(count(i))
p=max(r)
for i in r:
    if i==p:
        c+=1
print(c)