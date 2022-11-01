n=int(input())
x=list(map(int,input().split()))
e=[]
o=[]
for i in x:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
p=sum(e)
q=sum(o)
print(abs(p-q))