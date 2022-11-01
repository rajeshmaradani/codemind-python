n=int(input())
x=list(map(int,input().split()))
p,q=map(int,input().split())
s=0
for i in range(n):
    if x[i]<p or x[i]>q:
        s+=x[i]
print(s)        
        