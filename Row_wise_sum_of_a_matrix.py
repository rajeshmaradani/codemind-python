def rowsum(r,c,d):
    res=[0 for i in range(r)]
    for i in range(r):
        for j in range(c):
            res[i]+=d[i][j]
    return res
    
r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]
for i in range(r):
    vals=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=vals[j]
res=rowsum(r,c,d)
print(*res)