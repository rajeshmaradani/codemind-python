r,c=map(int,input().split())
row=[0 for i in range(c)]
sum=0
d=[row.copy() for i in range(r)]
for i in range(r):
    vals=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=vals[j]
for i in range(r):
    for j in range(c):
        sum+=d[i][j]
print(sum)