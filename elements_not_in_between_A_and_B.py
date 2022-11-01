n=int(input())
x=list(map(int,input().split()))
p,q=map(int,input().split())
e=0
for i in range(n):
    if x[i]<p or x[i]>q:
        e+=1
        print(x[i],end=" ")
if e==0:
    print(-1)