def count(s):
    r=[]
    c=0
    k=0
    for i in s:
        if i==" ":
            continue
        r.append(ord(i))
    m=min(r)
    m1=max(r)
    print(m1-m,end=" ")
    
s=input()
s=s.split()
for i in s:
    count(i)