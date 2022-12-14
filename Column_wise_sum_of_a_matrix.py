def rowsum(d,r,c):
    res=[0 for i in range(c)]
    for i in range(c):
        for j in range(r):
            res[i]+=d[j][i]
    return res        

r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]
for i in range(r):
    vals=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=vals[j]

res=rowsum(d,r,c)
print(*res)