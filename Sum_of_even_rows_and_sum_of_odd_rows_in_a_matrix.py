def even_oddrowsum(r,c,d):
    o=0
    e=0
    for i in range(r):
        for j in range(c):
            if i%2:
                o+=d[i][j]
            else:
                e+=d[i][j]
    return e,o
    

r,c=map(int,input().split())
row=[0 for i in range(c)]
sum=0
d=[row.copy() for i in range(r)]
for i in range(r):
    vals=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=vals[j]
res=even_oddrowsum(r,c,d)
print(*res)