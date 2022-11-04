n=int(input())
x=list(map(int,input().split()))
c=[]
a=sum(x)//n
for i in x:
    if i not in c:
        c.append(i)
for i in c:
    print (i,end=" ")
    