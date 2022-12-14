n,k=map(int,input().split())
a=list(map(int,input().split()))
r=[]
c=0
for i in a:
    x=str(i)
    p=len(x)
    if(i<0):
        p-=1
    if p==k:
        c+=1
print(c)