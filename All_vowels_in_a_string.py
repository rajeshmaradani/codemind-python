s=input()
r=[]
c=0
for j in s:
    if j=="a" or j=="e" or j=="i" or j=="o"or j=="u":
        r.append(j)
r1=set(r)
m="aeiou"
for i in m:
    if i not in r1:
        c+=1
if c==0:
    print("True")
else:
    print("False")