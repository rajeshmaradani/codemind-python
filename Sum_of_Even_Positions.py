n=int(input())
x=list(map(int,input().split()))
e=[]
for i in range(n):
    if i%2==0:
        e.append(x[i])
print(sum(e))        