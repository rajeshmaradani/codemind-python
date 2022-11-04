n=int(input())
x=list(map(int,input().split()))
c=0
a=sum(x)//n
for i in x:
    if i>=a:
        c+=1
print(c)        