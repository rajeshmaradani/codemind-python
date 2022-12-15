s=input()
c=0
r=[]
for j in s:
    if j=="a" or j=="e" or j=="i" or j=="o" or j=="u" or j=="A" or j=="E" or j=="I" or j=="O" or j=="U":
        if j not in r:
            c+=1
            r.append(j)
if c==0:
    print(-1)
else:
    print(*r)
    
        
        
