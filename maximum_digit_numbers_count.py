n=int(input())
a=list(map(int,input().split()))
r=[]
for i in a:
    x=str(i)
    p=len(x)
    if(i<0):
        p-=1
    r.append(p)
p1=max(r)
for i in a:
    x=str(i)
    p2=len(x)
    if(i<0):
        p2-=1
    if p2==p1:
        print(i,end=" ")