m,n=map(int,input().split())
N=list(map(int,input().split()))
M=list(map(int,input().split()))
c=0
k=0
N1=set(N)
M1=set(M)
for i in N1:
    if i not in M1:
        c+=1
for j in M1:
    if j not in N1:
        k+=1
print(k+c)