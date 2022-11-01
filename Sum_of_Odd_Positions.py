n=int(input())
x=list(map(int,input().split()))
o=[]
for i in range(n):
    if i%2==1:
        o.append(x[i])
print(sum(o))        