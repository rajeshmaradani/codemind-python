def count(s):
    r=[]
    for i in s:
        r.append(ord(i))
    m=min(r)
    m1=max(r)
    print(chr(m),chr(m1),end=" ")
s=input()
s=s.split()
for i in s:
    count(i)