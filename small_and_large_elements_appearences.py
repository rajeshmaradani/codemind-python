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
    for j in s:
        if chr(m)==j:
            c+=1
    for l in s:
        if l==chr(m1):
            k+=1
    print(chr(m),c,chr(m1),k)
    
s=input()
count(s)
