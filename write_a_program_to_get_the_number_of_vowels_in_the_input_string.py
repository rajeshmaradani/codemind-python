s=input()
r=[]
c=0
for j in s:
    if j=="a" or j=="e" or j=="i" or j=="o"or j=="u" or j=="A" or j=="E" or j=="I" or j=="O"or j=="U":
        c+=1
        r.append(j)
print(c)