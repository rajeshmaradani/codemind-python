n=int(input())
x=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if x[i-1]%2==1 and x[i+1]%2==1:
        if x[i]%2==1:
            c+=1
print(c)        