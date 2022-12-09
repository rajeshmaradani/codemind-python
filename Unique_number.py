n=int(input())
t=n
e=[]
while n>0:
    r=n%10
    e.append(r)
    n//=10
m=len(e)
g=set(e)
h=len(g)
if m==h:
    print("Unique Number")
else:
    print("Not Unique Number")